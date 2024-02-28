import java.io.*;

public class advent_23_1 {

	public static void main(String[] args) throws Exception
	{
		File file = new File ("..//advent-storage//advent-23-1.txt");
		BufferedReader br = new BufferedReader(new FileReader(file));
		String st;
		int result = 0;

		while ((st = br.readLine()) != null) {
			String[] digits = new String[st.length()];
			int numDigits = 0;
			for (char c: st.toCharArray()) {
				if (Character.isDigit(c)) {
					digits[numDigits] = String.valueOf(c);
					numDigits = numDigits + 1;
				}
			}
			String cal = digits[0].trim() + digits[numDigits - 1];
			int calVal = Integer.parseInt(String.valueOf(cal));
			result = result + calVal;		
		}
		System.out.println(result);
	}

}
