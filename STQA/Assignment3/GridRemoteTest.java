// File: src/main/java/com/sppu/tests/GridRemoteTest.java
package com.sppu.tests;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import java.net.URL;

public class GridRemoteTest {
    public static void main(String[] args) throws Exception {
        // If selenium-manager handles drivers, you don't need to set webdriver.* system property
        ChromeOptions options = new ChromeOptions();
        // Point to grid (standalone defaults to http://localhost:4444)
        URL gridUrl = new URL("http://localhost:4444");
        WebDriver driver = new RemoteWebDriver(gridUrl, options);
        driver.get("https://www.example.com");
        System.out.println("Remote Title: " + driver.getTitle());
        driver.quit();
    }
}
