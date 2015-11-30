package com.example.mitch.stewdy;


import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class ListArrayAdapter extends ArrayAdapter<String> {
    private final Context context;
    private final String[] values;

    public ListArrayAdapter(Context context, String[] values) {
        super(context, R.layout.list_tutor_preview, values);
        this.context = context;
        this.values = values;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater inflater = (LayoutInflater) context
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View rowView = inflater.inflate(R.layout.list_tutor_preview, parent, false);
        TextView textView = (TextView) rowView.findViewById(R.id.name);
        ImageView imageView = (ImageView) rowView.findViewById(R.id.logo);
        textView.setText(values[position]);

        // Change icon based on name
        String s = values[position];

        System.out.println(s);

        if (s.equals("Tutor1")) {
            imageView.setImageResource(R.drawable.test_face1);
        } else if (s.equals("Tutor2")) {
            imageView.setImageResource(R.drawable.test_face2);
        } else if (s.equals("Tutor3")) {
            imageView.setImageResource(R.drawable.test_face3);
        } else if (s.equals("Tutor4")) {
            imageView.setImageResource(R.drawable.test_face4);
        }

        return rowView;
    }
}