> 来源： http://icpc.baylor.edu/community/cmsicterface

Be aware of existence of [clics.ecs.baylor.edu](https://clics.ecs.baylor.edu) for contest control systems

* Web Service Spec
  * Authentication with Keycloak Token
  * Standings Upload
  * CLICS export
  * Contest export
  * CDP export
  * PC2 export
  * Attachments export
* MyICPC Web Service
  * Ping
  * Contest details
  * Contest sites
  * Contest teams
  * Contest institutions
  * Contest staff-members
  * Contest staff-member institutions
  * Contest social info
  * Contest questionnaires
  * Team detail
  * Team Past Results
  * Institution detail
  * Institution WF attendance

# Web Service Spec

**注意**
* 首先，在 “竞赛>导出>网络服务令牌”(`contest > exports > Web Services Tokens`) 创建一个网络服务接入令牌。选择您想用token实施的功能，（如 导出、上传、MyICPC网络服务）(Export, Standings Upload, MyICPC web services)
* 在URL中用比赛索引(Contest Key)指定比赛。比赛索引简如 `<比赛 abbreviation>-<年份>` ，例如：`World-Finals-2017`、`Central-Europe-2016`、`CTU-Open-2016`、`mcapgp-2016`

## 使用 Keycloak 令牌认证
To authenticate you need to acquire temporary token from Keycloak, based on your webservice access token. This token is then used with every request as bearer authentication. For every request you need new token, so the following line will be part of every request you make.

``` bash
curl -d "client_id=cm5-token" -d "username=token:<webservice access token>" -d "password=" -d "grant_type=password" "https://icpc.baylor.edu/auth/realms/cm5/protocol/openid-connect/token"
```
请求返回是个JSON，内容如下：
``` json
{
  "access_token": "<token>",
  "expires_in": 300,
  "refresh_expires_in":1800,
  "refresh_token":"<refresh_token>",
  "token_type":"bearer",
  "not-before-policy":0,
  "session_state":"<state>",
  "scope":"profile email"
}
```
将返回（`$res`）中的 `access_token` 提取出来存入 `$token` 中，以便后继使用
``` bash
token=`echo $res | sed 's/.*access_token":"//g' | sed 's/".*//g'`
```

## Standings Upload
You can upload the stanfings through rest API. The supported format for now is .csv, you can download the template from Contest Dashboard -> Conclusion -> Export Template.

``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/standings/upload/<contest key> -X POST -F "file=@<your standings file>" -H "Content-type:multipart/form-data" -H "Authorization: bearer $token"
```

## CLICS export
Export to zip file, produces .tsv tables with contest, groups, institutions and teams.

``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/export/CLICS/COMPOSITE/<contest key> -H "Authorization: bearer $token" > export_clics.zip
```

Export as Json:
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/export/CLICS/CONTEST/<contest key> -H "Authorization: bearer $token" > export_clics.json
```

## Contest export
Export contest data to zip file, produces .tab tables with contest, participants, staff, schools, sites and teams

``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/export/Contest/COMPOSITE/<contest key> -H "Authorization: bearer $token" > export_contest.zip
```

## CDP export
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/export/CDP/COMPOSITE/<contest key> -H "Authorization: bearer $token" > export_CDP.zip
```

## PC2 export
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/export/PC2/COMPOSITE/<contest key> -H "Authorization: bearer $token" > export_PC2.zip
```

## Attachments export
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/export/Attachments/COMPOSITE/<contest key> -H "Authorization: bearer $token" > export_attachments.zip
```

# MyICPC Web Service
Requires valid contest MyICPC token or contest manager credentials

## Ping
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/ping`
* param - contest key `{CTU-Open-2018}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/ping -H "Authorization: bearer $token"
```
样例输出：
``` json
{
  "code": "200",
  "message": "OK - contest: 42nd Annual World Finals of the International Collegiate Programming Contest"
}
```

## Contest details
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/details`
* param - contest key `{CTU-Open-2018}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/details -H "Authorization: bearer $token"
```
样例输出：
``` json
{
  "2409": {
    "name": "39th Annual World Finals of the ACM International Collegiate Programming Contest",
    "fullName": "39th Annual World Finals of the ACM International Collegiate Programming Contest",
    "shortName": "ACM-ICPC World Finals",
    "start": "2015-05-16",
    "end": "2015-05-21",
    "registrationStart": "2015-05-16",
    "registrationEnd": "2015-05-22",
    "key": "World-Finals-2015",
    "timeZone": "UTC",
    "hashtag": "#test"
    "hosts": "Name of the Host University",
    "access" : [ {
       "externalPersonId" : 4568,
       "username" : "test@test.com"
     } ]
  }
}
```

## Contest sites
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/sites`
* param - contest key `{CTU-Open-2018}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/sites -H "Authorization: bearer $token"
```
样例输出：
``` json
 {
   "sites": [
     {
       "id": 9574,
       "name": "Latin America",
       "location": "Marrakech",
       "type": "Normal"
     },
     {
       "id": 9571,
       "name": "North America",
       "location": "Marrakech",
       "type": "Normal"
     }
   ]
 }
```

## Contest teams
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/teams`
* param - contest key `{CTU-Open-2018}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/teams -H "Authorization: bearer $token"
```
样例输出：
``` json
{
  "teams": [
    {
      "externalReservationId": 11111,
      "name": "while(true);",
      "institutionId": 1111,
      "institutionUnitAliasId": 1111,
      "siteId": 123,
      "workstationId" : 85,
      "persons": [
        {
          "personId": 11,
          "externalReservationId": 11,
          "firstname": "Name",
          "lastname": "Name",
          "publicURLKey": "Key",
          "role": "Contestant",
          "badgeRole": "",
          "sex": "M",
          "contests": []
        },
        {
          "personId": 11,
          "externalReservationId": 11,
          "firstname": "Name",
          "lastname": "Name",
          "role": "Contestant",
          "badgeRole": "",
          "sex": "M",
          "contests": []
        },
        {
          "personId": 11,
          "externalReservationId": 11,
          "firstname": "Name",
          "lastname": "Name",
          "role": "Coach",
          "badgeRole": "",
          "sex": "F",
          "contests": []
        },
        {
          "personId": 11,
          "externalReservationId": 11,
          "firstname": "Name",
          "lastname": "Name",
          "publicURLKey": "Key",
          "role": "Contestant",
          "badgeRole": "",
          "sex": "M",
          "contests": []
        },
        {
          "personId": 11,
          "externalReservationId": 11,
          "firstname": "Name",
          "lastname": "Name",
          "publicURLKey": "Key",
          "role": "Attendee",
          "badgeRole": "Next Year Contestant",
          "sex": "M",
          "contests": []
        }
      ],
      "results": [
        {
          "externalContestId": 11,
          "contestName": "The XX Collegiate Programming Contest",
          "teamName": "while(true);",
          "institutionName": "Inst",
          "rank": 1,
          "problemssolved": 1,
          "totaltime": 900,
          "lastproblemtime": 200
        }
      ]
    }
  ]
}
```

## Contest institutions
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/institutions`
* param - contest key `{CTU-Open-2018}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/institutions -H "Authorization: bearer $token"
```
样例输出：
``` json
{
  "institutions": [
    {
      "institutionId": 11,
      "institutionUnitAliasId": 11,
      "name": "My University",
      "shortName": "Mu U",
      "twittername": "@MyU",
      "twitterhash": "#MyU",
      "facebookpage": "",
      "homepageurl": "http://www.my.u",
      "addressline1": "Add",
      "addressline2": "Add",
      "addressline3": "",
      "city": "Prague",
      "state": "",
      "zip": "12500",
      "country": "Czech",
      "latitude": 43.87374,
      "longitude": 125.34865
    }
  ]
}
```

## Contest staff-members
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/staff-members`
* param - contest key `{CTU-Open-2015}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/staff-members -H "Authorization: bearer $token"
```
样例输出：
``` json
{
  "persons": [
    {
      "personId": 11,
      "firstname": "Bob",
      "lastname": "Man",
      "publicURLKey": "key",
      "role": "Staff",
      "badgeRole": "North Africa and Middle East Contests - Director",
      "institutionUnitAliasId": 11,
      "contests": []
    },
    {
      "personId": 22,
      "firstname": "Boba",
      "lastname": "Mann",
      "role": "Staff",
      "badgeRole": "Host Student Volunteer / COE",
      "institutionUnitAliasId": 11,
      "contests": []
    }
  ]
}
```

## Contest staff-member institutions
*此接口**尚不支持**。如有需要请联系 manager@icpc.global 申请*

* GET : `icpc.baylor.edu/ws/myicpc/contest/{param}/staff-institutions`
* param - contest key `{CTU-Open-2015}`

样例输出：
``` json
{
  "institutions": [
    {
      "institutionId": 11,
      "institutionUnitAliasId": 11,
      "name": "My University",
      "shortName": "Mu U",
      "twittername": "@MyU",
      "twitterhash": "#MyU",
      "facebookpage": "",
      "homepageurl": "http://www.my.u",
      "addressline1": "Add",
      "addressline2": "Add",
      "addressline3": "",
      "city": "Prague",
      "state": "",
      "zip": "12500",
      "country": "Czech",
      "latitude": 43.87374,
      "longitude": 125.34865
    }
  ]
}
```

## Contest social info
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/social-info`
* param - contest key `{CTU-Open-2015}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/social-info -H "Authorization: bearer $token"
```

样例输出：
``` json
[
  {
    "externalPersonId": "11",
    "twitterUsername": null,
    "linkedinOauthToken": null,
    "linkedinOauthSecret": null
  }
]
```

## Contest questionnaires
*此接口**尚不支持**。如有需要请联系 manager@icpc.global 申请*

* GET : `icpc.baylor.edu/ws/myicpc/contest/{param}/questionnaires`
* param - contest key `{CTU-Open-2015}`

样例输出：
``` json
[
  {
    "externalPersonId": "11",
    "questionnaire": [
      {
        "question": "Question 4",
        "answer": "I really have no idea."
      },
      {
        "question": "Question 5",
        "answer": "Highest point of my future career would be to learn and contribute alongside the  leading experts of some field."
      }
    ]
  }
]
```

## Team detail
* GET : `https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/teams/123456`
* param - contest key `{Team-ID}`
``` bash
curl https://icpc.baylor.edu/cm5-contest-rest/rest/contest/myicpc/{param}/teams/123456 -H "Authorization: bearer $token"
```

样例输出：
``` json
[
  {
    "externalReservationId": 11,
    "name": "Name",
    "institutionId": 11,
    "institutionUnitAliasId": 11,
    "siteId": 11,
    "workstationId": 11,
    "persons": [
      {
        "personId": 11,
        "externalReservationId": 11,
        "firstname": "Name",
        "lastname": "Name",
        "role": "Contestant",
        "badgeRole": "",
        "sex": "M",
        "publicURLKey" : "key"
        "contests": [
          {
            "externalContestId": 11,
            "contestName": "Past Contest",
            "homepageUrl": " http://) ",
            "year": 2014,
            "role": "Contestant"
          },
          {
            "externalContestId": 12,
            "contestName": "North America Qualifier",
            "homepageUrl": " http://) ",
            "year": 2013,
            "role": "Contestant"
          }, ......
        ]
      }
    ]
  }
]
```

## Team Past Results
*此接口**尚不支持**。如有需要请联系 manager@icpc.global 申请*

* GET : `icpc.baylor.edu/ws/myicpc/team/{param}/past-results`
* param - contest key `{Team-ID}`

样例输出：
``` json
[
  {
    "externalContestId": 11,
    "contestName": "The Programming Contest",
    "teamName": "Name",
    "institutionName": "Inst",
    "rank": 3,
    "problemssolved": 6,
    "totaltime": 1307,
    "lastproblemtime": 287
  }
]
```

## Institution detail
*此接口**尚不支持**。如有需要请联系 manager@icpc.global 申请*

* GET : `icpc.baylor.edu/ws/myicpc/institution/{param}`
* param - contest key `{Institution-ID}`

样例输出：
``` json
[
  {
    "institutionId": 1,
    "institutionUnitAliasId": 11,
    "name": "University",
    "shortName": "Uni",
    "homepageurl": "www",
    "state": "",
    "country": "US"
  }
]
```

## Institution WF attendance
*此接口**尚不支持**。如有需要请联系 manager@icpc.global 申请*

* GET : `icpc.baylor.edu/ws/myicpc/institution/{param}/attend-wf`
* param - contest key `{Institution-ID}`

样例输出：
``` json
[
  {
    "id": 2409,
    "name": "39th Annual World Finals of the ACM International Collegiate Programming Contest"
  },
  {
    "id": 1811,
    "name": "38th Annual World Finals of the ACM International Collegiate Programming Contest"
  }
]
```