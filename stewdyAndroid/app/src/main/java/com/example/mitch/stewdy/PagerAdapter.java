package com.example.mitch.stewdy;

/**
 * Created by mitch on 2015-11-16.
 */
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;

public class PagerAdapter extends FragmentStatePagerAdapter {
    int mNumOfTabs;

    public PagerAdapter(FragmentManager fm, int NumOfTabs) {
        super(fm);
        this.mNumOfTabs = NumOfTabs;
    }

    @Override
    public Fragment getItem(int position) {

        switch (position) {
            case 0:
                TutorSessions tab1 = new TutorSessions();
                return tab1;
            case 1:
                TutorMessages tab2 = new TutorMessages();
                return tab2;
            case 2:
                TutorProfile tab3 = new TutorProfile();
                return tab3;
            case 3:
                TutorAccount tab4 = new TutorAccount();
                return tab4;
            default:
                return null;
        }
    }

    @Override
    public int getCount() {
        return mNumOfTabs;
    }
}