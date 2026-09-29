package ar.com.imaginar.appmuniruleta;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.webkit.ConsoleMessage;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.widget.TextView;
import android.widget.Toast;
import java.io.OutputStream;
import java.nio.charset.Charset;

public class MainActivity extends Activity {
    private static final int FILE_CHOOSER_REQUEST=901;
    private static final int EXPORT_JSON_REQUEST=902;
    private FrameLayout root;
    private WebView webView;
    private ValueCallback<Uri[]> fileCallback;
    private String pendingExportData;

    @Override protected void onCreate(Bundle b){
        super.onCreate(b);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        root=new FrameLayout(this);
        root.setBackgroundColor(Color.rgb(130,18,34));
        setContentView(root);
        try{createWebView();}catch(Throwable t){showNativeError("No se pudo iniciar La Bibliodera",t);}
        immersive();
    }

    @SuppressLint({"SetJavaScriptEnabled","JavascriptInterface"})
    private void createWebView(){
        webView=new WebView(this);
        webView.setBackgroundColor(Color.rgb(130,18,34));
        webView.setOverScrollMode(View.OVER_SCROLL_NEVER);
        webView.setVerticalScrollBarEnabled(false);
        webView.setHorizontalScrollBarEnabled(false);
        webView.setLongClickable(false);
        webView.setOnLongClickListener(new View.OnLongClickListener(){@Override public boolean onLongClick(View v){return true;}});
        WebSettings s=webView.getSettings();
        s.setJavaScriptEnabled(true);s.setDomStorageEnabled(true);s.setDatabaseEnabled(true);
        s.setAllowFileAccess(true);s.setAllowContentAccess(true);
        s.setSupportZoom(false);s.setBuiltInZoomControls(false);s.setDisplayZoomControls(false);
        s.setLoadWithOverviewMode(false);s.setUseWideViewPort(false);s.setTextZoom(100);
        if(Build.VERSION.SDK_INT>=16){s.setAllowFileAccessFromFileURLs(true);s.setAllowUniversalAccessFromFileURLs(false);}
        if(Build.VERSION.SDK_INT>=17)s.setMediaPlaybackRequiresUserGesture(false);

        webView.addJavascriptInterface(new Object(){
            @JavascriptInterface public void exportJson(final String name,final String data){
                runOnUiThread(new Runnable(){@Override public void run(){
                    pendingExportData=data==null?"{}":data;
                    try{
                        Intent i=new Intent(Intent.ACTION_CREATE_DOCUMENT);
                        i.addCategory(Intent.CATEGORY_OPENABLE);i.setType("application/json");
                        i.putExtra(Intent.EXTRA_TITLE,(name==null||name.length()==0)?"bibliodera-preguntas.json":name);
                        startActivityForResult(i,EXPORT_JSON_REQUEST);
                    }catch(Throwable e){pendingExportData=null;Toast.makeText(MainActivity.this,"No hay un administrador de archivos disponible.",Toast.LENGTH_LONG).show();}
                }});
            }
        },"AndroidBridge");

        webView.setWebChromeClient(new WebChromeClient(){
            @Override public boolean onConsoleMessage(ConsoleMessage m){return true;}
            @Override public boolean onShowFileChooser(WebView v,ValueCallback<Uri[]> cb,FileChooserParams p){
                if(fileCallback!=null)fileCallback.onReceiveValue(null);
                fileCallback=cb;
                try{Intent i=p.createIntent();i.addCategory(Intent.CATEGORY_OPENABLE);startActivityForResult(i,FILE_CHOOSER_REQUEST);return true;}
                catch(Throwable e){fileCallback=null;return false;}
            }
        });
        webView.setWebViewClient(new WebViewClient(){
            @Override public void onReceivedError(WebView v,WebResourceRequest r,WebResourceError e){if(Build.VERSION.SDK_INT>=23&&r!=null&&r.isForMainFrame())showWebError("Error WebView: "+String.valueOf(e.getDescription()));}
            @SuppressWarnings("deprecation") @Override public void onReceivedError(WebView v,int c,String d,String u){if(Build.VERSION.SDK_INT<23)showWebError("Error WebView "+c+": "+d);}
            @SuppressWarnings("deprecation") @Override public boolean shouldOverrideUrlLoading(WebView v,String u){return u!=null&&!u.startsWith("file:///android_asset/")&&!u.startsWith("#");}
        });
        root.addView(webView,new FrameLayout.LayoutParams(-1,-1));
        webView.loadUrl("file:///android_asset/index.html");
    }

    @Override protected void onActivityResult(int req,int result,Intent data){
        if(req==FILE_CHOOSER_REQUEST){
            Uri[] uris=WebChromeClient.FileChooserParams.parseResult(result,data);
            if(fileCallback!=null){fileCallback.onReceiveValue(uris);fileCallback=null;}return;
        }
        if(req==EXPORT_JSON_REQUEST){
            if(result==RESULT_OK&&data!=null&&data.getData()!=null&&pendingExportData!=null){
                try{OutputStream out=getContentResolver().openOutputStream(data.getData());if(out!=null){out.write(pendingExportData.getBytes(Charset.forName("UTF-8")));out.flush();out.close();Toast.makeText(this,"Copia guardada.",Toast.LENGTH_SHORT).show();}}
                catch(Throwable e){Toast.makeText(this,"No se pudo guardar la copia.",Toast.LENGTH_LONG).show();}
            }
            pendingExportData=null;return;
        }
        super.onActivityResult(req,result,data);
    }

    private void showWebError(String m){if(webView!=null)webView.loadData("<html><body style='margin:0;background:#8b1e1e;color:white;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center'><div><h2>La Bibliodera</h2><p>"+safe(m)+"</p></div></body></html>","text/html","UTF-8");}
    private String safe(String s){if(s==null)return "Error desconocido";return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");}
    private void showNativeError(String title,Throwable t){TextView v=new TextView(this);v.setTextColor(Color.WHITE);v.setBackgroundColor(Color.rgb(140,25,25));v.setTextSize(20f);v.setGravity(android.view.Gravity.CENTER);v.setPadding(40,40,40,40);v.setText(title+"\n\n"+t.getClass().getName()+"\n"+String.valueOf(t.getMessage()));root.removeAllViews();root.addView(v,new FrameLayout.LayoutParams(-1,-1));}
    @SuppressWarnings("deprecation") private void immersive(){try{getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY|View.SYSTEM_UI_FLAG_FULLSCREEN|View.SYSTEM_UI_FLAG_HIDE_NAVIGATION|View.SYSTEM_UI_FLAG_LAYOUT_STABLE|View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN|View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION);}catch(Throwable e){}}
    @Override public void onWindowFocusChanged(boolean f){super.onWindowFocusChanged(f);if(f)immersive();}
    @Override protected void onResume(){super.onResume();if(webView!=null)webView.onResume();immersive();}
    @Override protected void onPause(){if(webView!=null)webView.onPause();super.onPause();}
    @Override public void onBackPressed(){if(webView!=null)webView.loadUrl("javascript:(function(){if(location.hash&&location.hash!=='#ruleta'){location.hash='ruleta';}})()");else super.onBackPressed();}
    @Override protected void onDestroy(){if(fileCallback!=null){fileCallback.onReceiveValue(null);fileCallback=null;}if(webView!=null){root.removeView(webView);webView.destroy();webView=null;}super.onDestroy();}
}