
public class Solution {
    private static final int HEADER_SIZE = 4;

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String s : strs) {
            // Format length as 4-digit number with leading zeros
            String header = String.format("%04d", s.length());
            encoded.append(header).append(s);
        }
        return encoded.toString();
    }

    public List<String> decode(String s) {  // Fixed parameter name from 'str' to 's'
        List<String> result = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {
            // Read 4-digit length header
            String header = s.substring(i, i + HEADER_SIZE);
            int length = Integer.parseInt(header);
            i += HEADER_SIZE;
            
            // Read the actual string
            result.add(s.substring(i, i + length));
            i += length;
        }
        
        return result;
    }
}
