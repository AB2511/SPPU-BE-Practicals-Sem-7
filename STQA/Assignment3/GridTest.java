// File: src/main/java/com/sppu/tests/GridTest.java
package com.sppu.tests;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class GridTest {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver\\chromedriver.exe"); // if not using Selenium Manager
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.example.com");
        System.out.println("Title: " + driver.getTitle());
        driver.quit();
    }
}
