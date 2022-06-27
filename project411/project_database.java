import java.sql.*;
public class project_database {
    static String creatsql = "CREATE TABLE user("
    		+"email text UNIQUE primary key;);"
    		+ "CREATE TABLE course("
    		+"course_id VARCHAR(10) primary key;);"
    		+"CREATE TABLE post("
    		+"post_id VARCHAR(10) PRIMARY KEY,"
    		+"course_id FOREIGN KEY FROM course.course_id,"
    		+"user_id FOREIGN KEY FROM user.email,"
    		+"p_content text UNIQUE,"
    		+"p_date VARCHAR(8),"
    		+"headline text UNIQUE,);"
    		+"CREATE TABLE comment("
    		+"comment_id VARCHAR(10) PRIMARY KEY,"
    		+"post_id FOREIGN KEY FROM post.post_id,"
    		+"c_content text UNIQUE, "
    		+"c_date VARCHAR(8),);";
    final static String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    //
    final static String DB_URL = "jdbc:mysql://localhost/3306";
    //mysql用户名
    final static String name = "root";
    //mysql密码
    final static String pwd = "1031562613jie";
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        try{
            //register jdbc drive
            Class.forName(JDBC_DRIVER);
            //open the link
            conn = DriverManager.getConnection("jdbc:mysql://localhost/3306","root", "1031562613jie");
            //execute the query
            stmt = conn.createStatement();
            if(0 == stmt.executeLargeUpdate(creatsql)) {
                System.out.println("SUCCESS");
            }
            else {
                System.out.println("FAIL");
            }
            stmt.close();
            conn.close();
        }
        catch(Exception e) {
            System.out.println("FAIL IN CREATING THE TABLE");
            e.printStackTrace();
        }

    }
}
