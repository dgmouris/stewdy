package com.example.mitch.stewdy;

/**
 * Created by Mitch on 14/11/2015.
 */

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.AdapterView.OnItemSelectedListener;

public class FilterTutors extends AppCompatActivity implements View.OnClickListener {

    Button bShowTutors;
    EditText postal;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_filter_tutors);

        //fin tutors button
        bShowTutors = (Button) findViewById(R.id.bShowTutors);
        bShowTutors.setOnClickListener(this);

        //location radio
        postal =  (EditText) findViewById(R.id.postal);
        postal.setVisibility(View.INVISIBLE);

        //setup subject spinners
        Spinner subject = (Spinner) findViewById(R.id.subject_spinner);
        ArrayAdapter<CharSequence> subjectAdapter = ArrayAdapter.createFromResource(
                this, R.array.subject_array, R.layout.spinner_layout);
        subjectAdapter.setDropDownViewResource(R.layout.spinner_layout);
        subject.setAdapter(subjectAdapter);

        //setup area spinner
        Spinner area = (Spinner) findViewById(R.id.area_spinner);
        ArrayAdapter<CharSequence> areaAdapter = ArrayAdapter.createFromResource(
                this, R.array.area_array, R.layout.spinner_layout);
        areaAdapter.setDropDownViewResource(R.layout.spinner_layout);
        area.setAdapter(areaAdapter);

        //setup edu spinner
        Spinner edu = (Spinner) findViewById(R.id.edu_spinner);
        ArrayAdapter<CharSequence> eduAdapter = ArrayAdapter.createFromResource(
                this, R.array.edu_array, R.layout.spinner_layout);
        eduAdapter.setDropDownViewResource(R.layout.spinner_layout);
        edu.setAdapter(eduAdapter);


    }

    @Override
    public void onClick(View v){
        Intent about = new Intent(this, ListTutors.class);
        startActivity(about);

    }

    public void onRadioButtonClicked(View view) {
        // Is the button now checked?
        boolean checked = ((RadioButton) view).isChecked();

        // Check which radio button was clicked
        switch(view.getId()) {
            case R.id.radio_gps:
                if (checked)
                    // Use GPS location
                    postal.setVisibility(View.INVISIBLE);
                    break;
            case R.id.radio_postal:
                if (checked)
                    postal.setVisibility(View.VISIBLE);
                    // Use postal code
                    break;
        }
    }

}

