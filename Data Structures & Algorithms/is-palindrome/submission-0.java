class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replace(" ", "");
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        int sum = 0;
        boolean x = false;
        String z = "";

        for(int j = s.length()-1; j>=0; j--)
        {
            z = z+s.charAt(j);
        }
        x = s.equals(z);
        return x;
    }
}
