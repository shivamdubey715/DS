import java.rmi.*;

public class AddServer {
    public static void main(String args[]) {
        try { 
            // Create remote object
            AddServerImpl addServerImpl = new AddServerImpl(); 
            // Bind the remote object
            Naming.rebind("AddServer", addServerImpl);
        }
        catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }
}
