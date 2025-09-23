package com.sppu;

import jxl.Workbook;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import jxl.write.WriteException;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.logging.Level;
import java.util.logging.Logger;

public class CreateWriteExcelFile {

	private static final String EXCEL_FILE_LOCATION = "D:\\BE Practicals\\STQA\\STQAAsignment2\\TestCases.xls";

    public static void main(String[] args) {

        // Ensure folder exists
        Path directoryPath = Path.of(EXCEL_FILE_LOCATION).getParent();
        try {
            Files.createDirectories(directoryPath);
        } catch (IOException e) {
            throw new RuntimeException("Error creating directories", e);
        }

        WritableWorkbook workbook = null;

        try {
            workbook = Workbook.createWorkbook(new File(EXCEL_FILE_LOCATION));
            WritableSheet sheet = workbook.createSheet("SocialMediaTestCases", 0);

            // Header row
            sheet.addCell(new Label(0, 0, "Test Case ID"));
            sheet.addCell(new Label(1, 0, "Test Scenario"));
            sheet.addCell(new Label(2, 0, "Input"));
            sheet.addCell(new Label(3, 0, "Expected Result"));
            sheet.addCell(new Label(4, 0, "Actual Result"));
            sheet.addCell(new Label(5, 0, "Status"));

            // Example test case
            sheet.addCell(new Label(0, 1, "TC001"));
            sheet.addCell(new Label(1, 1, "Login with valid credentials"));
            sheet.addCell(new Label(2, 1, "username=abc; password=abc"));
            sheet.addCell(new Label(3, 1, "Login Successful"));
            sheet.addCell(new Label(4, 1, ""));
            sheet.addCell(new Label(5, 1, ""));

            workbook.write();
            System.out.println("Excel file created successfully at: " + EXCEL_FILE_LOCATION);

        } catch (IOException | WriteException e) {
            throw new RuntimeException(e);
        } finally {
            if (workbook != null) {
                try {
                    workbook.close();
                } catch (WriteException | IOException e) {
                    Logger logger = Logger.getLogger(CreateWriteExcelFile.class.getName());
                    logger.log(Level.SEVERE, "Error while closing workbook", e);
                }
            }
        }
    }
}
