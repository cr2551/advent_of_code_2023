import javax.swing.JFrame;

public class GearRatios {
    public static void main(String args[]) {
        JFrame myFrame = new JFrame();
        String title = "my window";
        int width = 300;
        int height = 100;
        myFrame.setTitle(title);
        // myFrame.getContentPane().add(emptyLabel, BorderLayout.CENTER);
        // myFrame.setSize(width, height);
        myFrame.setBounds(20, 20, width, height);
        myFrame.pack();
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setVisible(true);

    }
}