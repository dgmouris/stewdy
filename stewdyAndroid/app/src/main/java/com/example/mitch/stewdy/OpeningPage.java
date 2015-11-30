package com.example.mitch.stewdy;

/**
 * Created by Mitch for Stewdy on 14/11/2015.
 */
import android.content.SharedPreferences;
import android.graphics.Paint;
import android.preference.PreferenceManager;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.content.Intent;
import android.widget.EditText;
import android.widget.TextView;


import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class OpeningPage extends AppCompatActivity implements View.OnClickListener {

    Button bAbout, bBrowse, bRegisterStudent, bRegisterTutor;
    private EditText etUsername, etPassword;
    TextView Output;
    private SharedPreferences _preferences;
    private static final String COOKIE_KEY = "key";
    private static final String SESSION_COOKIE = "key";
    private static final String myurl = "http://stewdy.com/rest-auth/login/";
    private boolean auth = false;

    FloatingActionButton bLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_opening_page);
        _preferences = PreferenceManager.getDefaultSharedPreferences(this);


        bAbout = (Button) findViewById(R.id.bAbout);
        bAbout.setPaintFlags(bAbout.getPaintFlags() | Paint.UNDERLINE_TEXT_FLAG); //underlines the text

        bBrowse = (Button) findViewById(R.id.bBrowse);

        bLogin = (FloatingActionButton) findViewById(R.id.bLogin);

        etUsername = (EditText) findViewById(R.id.etUsername);
        etPassword = (EditText) findViewById(R.id.etPassword);

        Output = (TextView) findViewById(R.id.output);

        bRegisterStudent = (Button) findViewById(R.id.bRegisterStudent);
        bRegisterStudent.setPaintFlags(bRegisterStudent.getPaintFlags() | Paint.UNDERLINE_TEXT_FLAG); //underlines the text

        bRegisterTutor = (Button) findViewById(R.id.bRegisterTutor);
        bRegisterTutor.setPaintFlags(bRegisterTutor.getPaintFlags() | Paint.UNDERLINE_TEXT_FLAG); //underlines the text

        bAbout.setOnClickListener(this);
        bLogin.setOnClickListener(this);
        bBrowse.setOnClickListener(this);
        bRegisterStudent.setOnClickListener(this);
        bRegisterTutor.setOnClickListener(this);
    }

    @Override
    public void onClick(View v){
        switch(v.getId()) {
            case R.id.bAbout:
                Intent about = new Intent(this, About.class);
                startActivity(about);
                break;
            case R.id.bBrowse:
                Intent browse = new Intent(this, FilterTutors.class);
                startActivity(browse);
                break;
            case R.id.bLogin:
                attemptLogin();
                if (auth){
                    Intent TH = new Intent(this, TutorHome.class);
                    startActivity(TH);
                }else{
                    Output.setText(getString(R.string.auth_error));
                }
                break;
            case R.id.bRegisterStudent:
                Intent RS = new Intent(this, RegisterStudent.class);
                startActivity(RS);
                break;
            case R.id.bRegisterTutor:
                Intent RT = new Intent(this, RegisterTutor.class);
                startActivity(RT);
                break;
        }
    }

    private void attemptLogin(){
        Map<String, String> params = new HashMap<>();
        params.put("username", etUsername.getText().toString());
        params.put("password", etPassword.getText().toString());

        JSONObject jsonObj = new JSONObject(params);

        RequestQueue queue = Volley.newRequestQueue(this);
        JsonObjectRequest jsObjRequest = new JsonObjectRequest(Request.Method.POST,myurl,jsonObj,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        getHeaders(response);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        VolleyLog.e("Error: ", error.getMessage());
                    }
                });
        queue.add(jsObjRequest);
    }

    protected void getHeaders(JSONObject response) {
        String cookie;
        try {
            cookie = (String) response.get(COOKIE_KEY);
            auth = true;
        }catch(Exception e){
            cookie = "";
            VolleyLog.e("Error: ","Token error.");
            }
        SharedPreferences.Editor prefEditor = _preferences.edit();
        prefEditor.putString(SESSION_COOKIE, cookie);
        prefEditor.commit();
    }

}

