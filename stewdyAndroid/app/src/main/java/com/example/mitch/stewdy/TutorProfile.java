package com.example.mitch.stewdy;

/**
 * Created by mitch on 2015-11-16.
 */
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.content.ContextCompat;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

public class TutorProfile extends Fragment {
    //test data
    private String[] tutor1 = {"John D", "Credentials", "Short Biograhy"};

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view =  inflater.inflate(R.layout.tutor_profile, container, false);

        TextView tutorName = (TextView) view.findViewById(R.id.DisplayName);
        tutorName.setText(tutor1[0]);

        TextView tutorCred = (TextView) view.findViewById(R.id.cred);
        tutorCred.setText(tutor1[1]);

        TextView tutorBio = (TextView) view.findViewById(R.id.bio);
        tutorBio.setText(tutor1[2]);

        ImageView profilePic = (ImageView) view.findViewById(R.id.profilePic);
        profilePic.setImageDrawable(ContextCompat.getDrawable(this.getContext(), R.drawable.test_face1));




        return view;
    }

}
