package com.example.appengine.users;

import com.google.appengine.api.users.UserService;
import com.google.appengine.api.users.UserServiceFactory;

import java.io.IOException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


//https://cloud.google.com/appengine/docs/java/users/

//User authentication in Java

/* 
The following example greets a user who has signed in to the app with a personalized message and a link to sign out.
If the user is not signed in, the app offers a link to the sign-in page for Google Accounts.

You can test if the user is signed in and get the user's email address using the standard servlet API, with the request object's getUserPrincipal() method. 
You can use the User service API to generate sign-in and sign-out URLs.
 */




//Authenicating google Accounts
public class UsersServlet extends HttpServlet 
{

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws IOException 
  {
    UserService userService = UserServiceFactory.getUserService();

    String thisUrl = req.getRequestURI();

    resp.setContentType("text/html");

    if (req.getUserPrincipal() != null) 
    {
      resp.getWriter().println("<p>Hello, "
          + req.getUserPrincipal().getName()
          + "!  You can <a href=\""
          + userService.createLogoutURL(thisUrl)
          + "\">sign out</a>.</p>");
    } 

    else
    {
      resp.getWriter().println("<p>Please <a href=\"" 
        + userService.createLoginURL(thisUrl) 
        + "\">sign in</a>.</p>");
    }


  }

}

//Task to be completed tomorrow https://developers.google.com/identity/protocols/OpenIDConnect


//Auth 2.0 and OpenID Connect

//OpenID Connect is an identity layer on top of the OAuth 2.0 protocol. You can use the directions provided in our OpenID Connect documentation to set up OAuth 2.0 and authenticate users.

//Our implementation of OpenID Connect on OAuth 2.0 conforms to the OpenID Connect specification, and is OpenID Certified.


//To learn how to set security constraints for URLs, see The Deployment Descriptor: Security and Authentication for web.xml.

// Implementation below


