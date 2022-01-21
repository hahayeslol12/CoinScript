import java.io.FileWriter;  
import java.io.IOException; 

public class FilePatcher {
  public static void main(String[] args) {
    try {
      FileWriter myWriter = new FileWriter("main.py");
      myWriter.write("not yet done.");
      myWriter.close();
      System.out.println("Successfully wrote to the file.");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}
