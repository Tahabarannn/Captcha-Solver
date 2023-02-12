package btkCaptcha;

import java.io.File;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.io.FileHandler;

import io.github.bonigarcia.wdm.WebDriverManager;
import net.sourceforge.tess4j.ITesseract;
import net.sourceforge.tess4j.Tesseract;



public class BtkCaptcha_Solver {

	public static void main(String[] args) throws IOException, Exception {
		
		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver();
		
		try {
			driver.manage().window().maximize();
			driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
			
			driver.get("https://internet2.btk.gov.tr/sitesorgu/");
			
			String Domain = "www.example.com";
			
			driver.findElement(By.xpath("/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/input[1]")).sendKeys(Domain);
			
			WebElement imageelement = driver.findElement(By.xpath("/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[4]/img"));
			
			File src = imageelement.getScreenshotAs(OutputType.FILE);
			
			String path="C:\\Users\\Administrator\\OneDrive\\Masaüstü\\BTK2\\captchaimages.png";
			
			FileHandler.copy(src, new File(path));
			
			Thread.sleep(2000);
			
			ITesseract image = new Tesseract();
			
			String str = image.doOCR(new File(path));
			
			System.out.println("Image OCR done");
			System.out.println(str);
			
			String Captcha = str.replaceAll("[^a-zA-Z0-9]", "");
			
			driver.findElement(By.xpath("/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/form/div[4]/input")).sendKeys(Captcha);
			
			driver.findElement(By.xpath("/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div[1]/input")).click();
			
			Thread.sleep(1500);
			
			String Check = driver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div/div/div[4]/div/div[3]/a/div/span[1]")).getText();
			
			Boolean Check2 = Boolean.parseBoolean(Check);
			
			
			if ( Check2 = true ) {
				
			    Runtime runtime = Runtime.getRuntime();
			    Process p1 = runtime.exec("C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe \"C:\\Users\\Administrator\\OneDrive\\Masaüstü\\BTK2\\script_python.py");
			    System.out.print("is process alive = "+p1.isAlive());
				System.out.println("OK");
				driver.quit();
				
			} else {
				driver.quit();
			}
			
			
				
				
		} catch (Exception e) {
			System.out.println("exception caught :" + e.getMessage());
			driver.quit();
			
		}
			

	}

}
