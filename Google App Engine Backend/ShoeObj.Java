//Java Backend Functions


// AutoComplete Implementation //

import java.io.*;

public class ShoeObj 
{ 
	string name;
    string lprice;
    string sURL;
    string imgURL;
    List sizes = new ArrayList();

	public ShoeObj (name, lprice, sURL, imgURL)
	{
      this.name = name;
      this.lprice = lprice;
      this.sURL=sURL
      this.imgURL = imgURL;
      getSizes();
  	}


	public void getSizes ()
	{
		// code to get sizes and price differences from URL
        // tree = htmlTree (sURL)
        // sizes.addall((map (str.strip, tree.xpath()))) # sizes
   	}
        

    def namelist (self):
        print ('\"' +self.name +'\",') ##.replace('*', '') #Print out shoelist names

    def shoelist (self):
        print ('"' ,self.name, '|', self.lprice ,'|' , self.URL ,'|' , self.sizes , '|' ,self.imgURL,'",') #Print out full shoe information

}