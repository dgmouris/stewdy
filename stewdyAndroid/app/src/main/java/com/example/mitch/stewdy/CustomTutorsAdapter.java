package com.example.mitch.stewdy;

import android.content.Context;

/**
 * Created by mitch on 2015-12-02.
 */
import java.util.ArrayList;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.RatingBar;
import android.widget.TextView;

public class CustomTutorsAdapter extends ArrayAdapter<Tutor> {

    public CustomTutorsAdapter(Context context, ArrayList<Tutor> tutors) {
        super(context, 0, tutors);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // Get the data item for this position
        Tutor tutor = getItem(position);
        // Check if an existing view is being reused, otherwise inflate the view
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.list_tutor_preview, parent, false);
        }
        // Lookup view for data population
        TextView firstName = (TextView) convertView.findViewById(R.id.name);
        TextView userName = (TextView) convertView.findViewById(R.id.username);
        TextView specialization = (TextView) convertView.findViewById(R.id.specialization);
        TextView education = (TextView) convertView.findViewById(R.id.education);
        TextView bio = (TextView) convertView.findViewById(R.id.bio);
        RatingBar stars = (RatingBar) convertView.findViewById(R.id.ratingBar);

        // Populate the data into the template view using the data object
        firstName.setText(tutor.getFirstName());
        userName.setText("("+tutor.getUserName()+")");
        specialization.setText(tutor.getSpecialization());
        education.setText(tutor.getEducation());
        bio.setText(tutor.getBio());
        stars.setRating(tutor.getRating());
        // Return the completed view to render on screen
        return convertView;
    }
}
