package com.example.mitch.stewdy;

import android.app.ListActivity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;

import java.util.ArrayList;

/**
 * Created by mitch on 2015-12-02.
 */
public class CreateTutorList extends ListActivity{
    JSONArray jArray;
    private static String myurl = "http://stewdy.com/reviews/api/v1/tutor/";
    TextView Output;
    CustomTutorsAdapter adapter;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_tutors);
        Output = (TextView) findViewById(R.id.TextOutput);
        Output.setText("Finding tutors near you...");
        downloadList();
    }

    @Override
    protected void onListItemClick(ListView l, View v, int position, long id) {
        //get selected items
        Tutor selectedTutor = adapter.getItem(position);
        String clicked = selectedTutor.getUserName()+"\n You must be logged in to see the whole profile/book a tutor.";
        Toast.makeText(this, clicked, Toast.LENGTH_LONG).show();

    }


    private void populateTutorsList() {
        // Construct the data source
        ArrayList<Tutor> arrayOfTutors = Tutor.fromJsonArray(jArray);
        // Create the adapter to convert the array to views
        adapter = new CustomTutorsAdapter(this, arrayOfTutors);
        // Attach the adapter to a ListView
        //ListView listView = (ListView) findViewById(R.id.list);
        ListView listView = getListView();
        listView.setAdapter(adapter);

    }

    private void downloadList(){
        RequestQueue queue = Volley.newRequestQueue(this);

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, myurl,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                        //Output.setText(response.toString());
                        try{
                            jArray = new JSONArray(response);
                            Output.setText("Tutors near you");
                            populateTutorsList();
                        }catch (JSONException e){
                            //some json error
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                //some volley request error
            }
        });
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }


}
