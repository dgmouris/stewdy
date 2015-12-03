package com.example.mitch.stewdy;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

/**
 * Created by mitch on 2015-12-02.
 */
public class Tutor {

    private JSONObject user;
        private String username;
        private String first_name;
        private String last_name;
        private String email;

    private String bio;
    private String education;
    private String specialization;
    private String imageUrl;
    private float rating;

    //Series of getters to access the declared fields

    public JSONObject user(){
        return this.user;
    }
    public String getFirstName() {
        return this.first_name;
    }
    public String getUserName() {
        return this.username;
    }

    public float getRating() {
        return this.rating;
    }
    public String getEducation() {
        return this.education;
    }
    public String getSpecialization() {
        return this.specialization;
    }
    public String getBio() {
        return this.bio;
    }
    //public String getImageUrl() {
    //    send volley request for image here?
    //    return this.imageUrl;
    //}

    public static Tutor fromJson(JSONObject jsonObject) {
        Tutor t = new Tutor();
        // Deserialize json into object fields
        try {
            t.user = jsonObject.getJSONObject("user");
                t.first_name = t.user.getString("first_name");
                //t.last_name = jsonObject.getString("last_name");
                t.username = t.user.getString("username");
                ////t.email = jsonObject.getString("email");
            t.specialization = jsonObject.getString("specialization");
            t.education = jsonObject.getString("education");
            t.bio = jsonObject.getString("bio");
            t.rating = Float.parseFloat(jsonObject.getString("rating"));
            //t.imageUrl = jsonObject.getString("image_url");
        } catch (JSONException e) {
            e.printStackTrace();
            return null;
        }
        // Return new object
        return t;
    }

    // Decodes array of tutor json results into tutor model objects
    public static ArrayList<Tutor> fromJsonArray(JSONArray jsonArray) {
        ArrayList<Tutor> tutors = new ArrayList<Tutor>(jsonArray.length());
        // Process each result in json array, decode and convert to tutor object
        for (int i=0; i < jsonArray.length(); i++) {
            JSONObject tutorJson = null;
            try {
                tutorJson = jsonArray.getJSONObject(i);
            } catch (Exception e) {
                e.printStackTrace();
                continue;
            }

            Tutor tutor = Tutor.fromJson(tutorJson);
            if (tutor != null) {
                tutors.add(tutor);
            }
        }
        return tutors;
    }
}