> 来源： http://icpc.baylor.edu/community/openid

> **已弃用**，迁移至KeyCloak

# Introduction
ICPC allows you to authenticate your users through their ICPC credentials and receive basic information to perform authorization. 

We provide a dedicated server at https://openid.ecs.baylor.edu that uses OpenID Connect identity layer on top of the OAuth 2.0 protocol. More details can be found at http://openid.net/connect/. Simply, it allows Clients to verify the identity of the End-User based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User in an interoperable and REST-like manner.

# Live demo
You can play with a live demo that uses JavaScript and performs authentication and authorises the user in global/contest context.

Consider the [https://openid.ecs.baylor.edu/global/](https://icpc.baylor.edu/auth/realms/cm5/) demo that allows you to login to the system using ICPC credentials. Profile and token carry a useful user information. 

The second demo at [https://openid.ecs.baylor.edu/wf2015/]() that allows you the same although the first demo provides user roles in general global context and the second one within world finals

# Provided roles
The Authorization Server determines the following roles in given context:
``` json
"roles": [
      "teamMember",
      "contestManager",
      "staffMember",
      "user",
      "coach"
    ]
```
The "user" role is determined based on end users relation to given contest (has at least any other role). 

# Usage for local contest
Contact ICPC manager in the ICPC contact page with your inquiry. Before that start with making a demo first.

You can consider the variety of examples shipped with Keycloak server http://keycloak.jboss.org/, the most basic example needs a single file. The live demo uses example called js-console, and we suggest you start with it. What you need to run the example is a web server. Keycloak is shipped with Wildfly 9 server, which you can use.

Attached is a sample web archive with demo application and configuration that allows you to run the demo towards our server while expecting you connecting from http://URL 127.0.0.1:8080 or http://localhost:8080 (other URLs are rejected). You can unzip the war to see the details, it contains an HTML file, JavaScript and JSON configuration that is the most important. It states the configuration: 

``` json
{
  "realm" : "localhostdemo",
  "realm-public-key" : "..",
  "auth-server-url" : "https://openid.ecs.baylor.edu/",
  "ssl-required" : "true",
  "resource" : "global",
  "public-client" : true
}
```

The configuration specifies the authorisation server, the realm (scope) for which you are authorised and resource (a clientId). Resource is the context of authorisation global or contest abbreviations - such as World-Finals-2015

We authorise you two clientIDs/resources global and World-Finals-2015 and can develop your application toward them.

Although for production use in the context of your contest you need to request us to register your private realm/clientID. 

See the Keycloak documentation and examples for setting details and options (private key, allowed URLs for authentication, allowed web origins for CORS - cross-origin resource sharing, clientID, etc.) you can also request a required role to authenticate (user/contest manager, etc) as by default all ICPC user authenticate no matter relation to your contest.

# Endpoints and Metadata
These can be found at [https://openid.ecs.baylor.edu/realms/global/.well-known/openid-configuration](https://icpc.baylor.edu/auth/realms/cm5/.well-known/openid-configuration)