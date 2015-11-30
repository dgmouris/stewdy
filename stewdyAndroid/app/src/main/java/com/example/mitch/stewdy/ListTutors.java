package com.example.mitch.stewdy;


import android.app.ListActivity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import android.view.View;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;


import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class ListTutors extends ListActivity {

    private TextView Output;
    private static String myurl = "http://stewdy.com/reviews/api/v1/tutor/";
    private JSONObject jArray;

    // JSON key names
    private static final String TAG_FIRST_NAME = "first_name";
    private static final String TAG_LAST_NAME = "last_name";
    private static final String TAG_RATING = "rating";
    private static final String TAG_EDUCATION = "education";
    private static final String TAG_BIO = "bio";

    static final String[] Tutor_List =
             new String[] { "Tutor1", "Tutor2", "Tutor3", "Tutor4"};

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_tutors);
        setListAdapter(new ListArrayAdapter(this, Tutor_List));
        //Output = (TextView) findViewById(R.id.output);
        //downloadList();

    }

    @Override
    protected void onListItemClick(ListView l, View v, int position, long id) {

        //get selected items
        String selectedValue = (String) getListAdapter().getItem(position);
        Toast.makeText(this, selectedValue, Toast.LENGTH_SHORT).show();

    }


    private void downloadList(){
        RequestQueue queue = Volley.newRequestQueue(this);

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, myurl,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                        Output.setText(response.substring(0, 500));

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Output.setText("That didn't work!");
            }
        });
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }

}