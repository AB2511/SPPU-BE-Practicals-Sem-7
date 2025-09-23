package sppu;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class LoginTest {

    public static void main(String[] args) {
        // Set ChromeDriver path
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver\\chromedriver.exe");

        WebDriver driver = new ChromeDriver();

        try {
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));

            // URL of your login page
            String url = "http://localhost/STQAssignment1/index.html";

            // ---------------- POSITIVE TEST ----------------
            System.out.println("===== POSITIVE LOGIN TEST =====");
            driver.get(url);
            WebElement username = driver.findElement(By.id("username"));
            WebElement password = driver.findElement(By.id("password"));
            WebElement loginBtn = driver.findElement(By.id("login"));

            username.clear();
            username.sendKeys("abc");
            password.clear();
            password.sendKeys("abc");
            loginBtn.click();

            Thread.sleep(500);
            if (driver.getPageSource().contains("Login Successful...!")) {
                System.out.println("PASS: Valid login");
            } else {
                System.out.println("FAIL: Valid login");
            }

            // ---------------- NEGATIVE TESTS ----------------
            System.out.println("\n===== NEGATIVE LOGIN TESTS =====");

            // 1. Invalid username + invalid password
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            loginBtn = driver.findElement(By.id("login"));

            username.clear();
            username.sendKeys("wrongUser");
            password.clear();
            password.sendKeys("wrongPass");
            loginBtn.click();
            Thread.sleep(500);
            if (driver.getPageSource().contains("Authentication failed...!")) {
                System.out.println("PASS: Invalid username & password");
            } else {
                System.out.println("FAIL: Invalid username & password");
            }

            // 2. Valid username + invalid password
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            loginBtn = driver.findElement(By.id("login"));

            username.clear();
            username.sendKeys("abc");
            password.clear();
            password.sendKeys("wrongPass");
            loginBtn.click();
            Thread.sleep(500);
            if (driver.getPageSource().contains("Authentication failed...!")) {
                System.out.println("PASS: Valid username + invalid password");
            } else {
                System.out.println("FAIL: Valid username + invalid password");
            }

            // 3. Invalid username + valid password
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            loginBtn = driver.findElement(By.id("login"));

            username.clear();
            username.sendKeys("wrongUser");
            password.clear();
            password.sendKeys("abc");
            loginBtn.click();
            Thread.sleep(500);
            if (driver.getPageSource().contains("Authentication failed...!")) {
                System.out.println("PASS: Invalid username + valid password");
            } else {
                System.out.println("FAIL: Invalid username + valid password");
            }

            // 4. Blank username
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            loginBtn = driver.findElement(By.id("login"));

            username.clear();
            password.clear();
            password.sendKeys("abc");
            loginBtn.click();
            Thread.sleep(500);
            if (driver.getPageSource().contains("Authentication failed...!")) {
                System.out.println("PASS: Blank username");
            } else {
                System.out.println("FAIL: Blank username");
            }

            // 5. Blank password
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            loginBtn = driver.findElement(By.id("login"));

            username.clear();
            username.sendKeys("abc");
            password.clear();
            loginBtn.click();
            Thread.sleep(500);
            if (driver.getPageSource().contains("Authentication failed...!")) {
                System.out.println("PASS: Blank password");
            } else {
                System.out.println("FAIL: Blank password");
            }

            // 6. Leading space in password
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            loginBtn = driver.findElement(By.id("login"));

            username.clear();
            username.sendKeys("abc");
            password.clear();
            password.sendKeys(" abc"); // space before
            loginBtn.click();
            Thread.sleep(500);
            if (driver.getPageSource().contains("Authentication failed...!")) {
                System.out.println("PASS: Leading space in password");
            } else {
                System.out.println("FAIL: Leading space in password");
            }

            // 7. Check placeholder text (UI test)
            driver.get(url);
            username = driver.findElement(By.id("username"));
            password = driver.findElement(By.id("password"));
            if ("Enter Name".equals(username.getAttribute("placeholder")) &&
                "Enter Password".equals(password.getAttribute("placeholder"))) {
                System.out.println("PASS: Placeholder text is correct");
            } else {
                System.out.println("FAIL: Placeholder text check");
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
}
