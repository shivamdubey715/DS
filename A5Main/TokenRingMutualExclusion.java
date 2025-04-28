import java.util.concurrent.Semaphore;

public class TokenRingMutualExclusion {
    private static final int NUM_PROCESSES = 5; // Number of processes in the ring
    private static Semaphore token = new Semaphore(1); // Semaphore for token control
    private static int currentProcess = 0; // Index of the current process
    private static String[] messageBuffer = new String[NUM_PROCESSES]; // Message buffer

    public static void main(String[] args) {
        for (int i = 0; i < NUM_PROCESSES; i++) {
            new Thread(new Process(i)).start();
        }
    }

    static class Process implements Runnable {
        private int processId;

        public Process(int processId) {
            this.processId = processId;
        }

        @Override
        public void run() {
            while (true) {
                try {
                    // Non-critical section
                    Thread.sleep(1000);

                    // Entering critical section
                    token.acquire();
                    if (currentProcess == processId) {
                        System.out.println("Process " + processId + " is in the critical section.");
                        // Perform critical section operations here
                        if (messageBuffer[processId] != null) {
                            System.out.println("Message received by Process " + processId + ": " + messageBuffer[processId]);
                            messageBuffer[processId] = null; // Clear the message buffer after processing
                        }

                        // Message passing logic
                        int receiver = (processId + 1) % NUM_PROCESSES;
                        if (messageBuffer[receiver] == null) {
                            // Send message if the receiver's buffer is empty
                            String message = "Message from Process " + processId;
                            System.out.println("Process " + processId + " sending message: " + message);
                            messageBuffer[receiver] = message;
                        }

                        // Exit critical section
                        System.out.println("Process " + processId + " exits the critical section.");
                        currentProcess = (currentProcess + 1) % NUM_PROCESSES; // Pass the token
                    }
                    token.release();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}