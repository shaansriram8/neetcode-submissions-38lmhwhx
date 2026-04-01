class Solution {
    public boolean isAnagram(String s, String t) {
        boolean x = false;
        int sum1 = 0;
        int sum2 =0;
        int prod1 = 1;
        int prod2 = 1;
        if(s.length() == t.length())
        {
            for(int i =0; i<s.length(); i++)
            {
                sum1+= s.charAt(i);
                sum2+= t.charAt(i);
                prod1*= s.charAt(i);
                prod2*= t.charAt(i);
            }
            if(sum1 == sum2 && prod1 == prod2)
            {
            x = true;
            }
        }
        
        return x;

    }
}
