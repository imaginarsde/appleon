package ar.com.imaginar.appleon;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.webkit.ConsoleMessage;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.widget.TextView;

public class MainActivity extends Activity {
    private FrameLayout root;
    private WebView webView;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        root=new FrameLayout(this); root.setBackgroundColor(Color.rgb(5,8,6)); setContentView(root);
        try { createWebView(); } catch(Throwable t) { showNativeError("No se pudo iniciar la experiencia León",t); }
        immersive();
    }

    @SuppressLint("SetJavaScriptEnabled")
    private void createWebView() {
        webView=new WebView(this); webView.setBackgroundColor(Color.BLACK); webView.setOverScrollMode(View.OVER_SCROLL_NEVER);
        webView.setVerticalScrollBarEnabled(false); webView.setHorizontalScrollBarEnabled(false);
        webView.setOnLongClickListener(new View.OnLongClickListener(){ @Override public boolean onLongClick(View v){ return true; }}); webView.setLongClickable(false);
        WebSettings s=webView.getSettings(); s.setJavaScriptEnabled(true); s.setDomStorageEnabled(true); s.setAllowFileAccess(true); s.setAllowContentAccess(false); s.setSupportZoom(false); s.setBuiltInZoomControls(false); s.setDisplayZoomControls(false); s.setLoadWithOverviewMode(false); s.setUseWideViewPort(false); s.setTextZoom(100); if(Build.VERSION.SDK_INT>=17)s.setMediaPlaybackRequiresUserGesture(false);
        webView.setWebChromeClient(new WebChromeClient(){ @Override public boolean onConsoleMessage(ConsoleMessage message){ return true; }});
        webView.setWebViewClient(new WebViewClient(){
            @Override public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error){ if(Build.VERSION.SDK_INT>=23&&request!=null&&request.isForMainFrame())showWebError("Error WebView: "+String.valueOf(error.getDescription())); }
            @SuppressWarnings("deprecation") @Override public void onReceivedError(WebView view,int errorCode,String description,String failingUrl){ if(Build.VERSION.SDK_INT<23)showWebError("Error WebView "+errorCode+": "+description); }
            @SuppressWarnings("deprecation") @Override public boolean shouldOverrideUrlLoading(WebView view,String url){ return url!=null&&!url.startsWith("file:///android_asset/"); }
        });
        root.addView(webView,new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,ViewGroup.LayoutParams.MATCH_PARENT));
        webView.loadUrl("file:///android_asset/index.html");
    }
    private void showWebError(String message){ if(webView!=null){ String safe=message==null?"Error desconocido":message.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"); webView.loadData("<html><body style='margin:0;background:#8b1e1e;color:white;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center'><div><h2>León Interactivo</h2><p>"+safe+"</p></div></body></html>","text/html","UTF-8"); }}
    private void showNativeError(String title,Throwable t){ TextView v=new TextView(this);v.setTextColor(Color.WHITE);v.setBackgroundColor(Color.rgb(140,25,25));v.setTextSize(20f);v.setGravity(android.view.Gravity.CENTER);v.setPadding(40,40,40,40);v.setText(title+"\n\n"+t.getClass().getName()+"\n"+String.valueOf(t.getMessage()));root.removeAllViews();root.addView(v,new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,ViewGroup.LayoutParams.MATCH_PARENT)); }
    @SuppressWarnings("deprecation") private void immersive(){ try{ getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY|View.SYSTEM_UI_FLAG_FULLSCREEN|View.SYSTEM_UI_FLAG_HIDE_NAVIGATION|View.SYSTEM_UI_FLAG_LAYOUT_STABLE|View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN|View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION); }catch(Throwable ignored){} }
    @Override public void onWindowFocusChanged(boolean hasFocus){ super.onWindowFocusChanged(hasFocus); if(hasFocus)immersive(); }
    @Override protected void onResume(){ super.onResume(); if(webView!=null)webView.onResume(); immersive(); }
    @Override protected void onPause(){ if(webView!=null)webView.onPause(); super.onPause(); }
    @Override protected void onDestroy(){ if(webView!=null){ root.removeView(webView); webView.destroy(); webView=null; } super.onDestroy(); }
}