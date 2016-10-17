//Java Backend Functions
// AutoComplete Implementation //

import java.io.*;
import java.lang.*;

public class ShoeObj
{
		string name;
    string lprice;
    string sURL;
    string imgURL;
		List<String> xpaths = new ArrayList<String>(); // Size(button), Price

    List sizes = new ArrayList();
		Pair<Integer, Integer> sizePrice = new Pair<>();

	public ShoeObj (name, lprice, sURL, imgURL)
	{
      this.name = name;
      this.lprice = lprice;
      this.sURL=sURL
      this.imgURL = imgURL;
      getSizes();
			getPrices();
  	}


	public void getSizes ()
	{
		// code to get sizes and price differences from URL
        // tree = htmlTree (sURL)
        // sizes.addall((map (str.strip, tree.xpath()))) # sizes
   	}

	public void getPrices()
	{
			// code to update price based on size collected
			//implement a web scraping feature that can click the button of the size desired and return a price if selection exists
	}


    def namelist (self):
        print ('\"' +self.name +'\",') ##.replace('*', '') #Print out shoelist names

    def shoelist (self):
        print ('"' ,self.name, '|', self.lprice ,'|' , self.URL ,'|' , self.sizes , '|' ,self.imgURL,'",') #Print out full shoe information

}
