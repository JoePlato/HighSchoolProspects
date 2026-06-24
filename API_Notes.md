**Rivals**





The basic API Response looks a little like this with the list attribute having a list of dictionary containing player data. If there is no players the list parameter remains blank







"pageProps": {

&nbsp;       "pageType": "database",

&nbsp;       "searchData": {

&nbsp;           "pagination": {

&nbsp;               "count": 9932,

&nbsp;               "offset": 9925,

&nbsp;               "limit": 25,

&nbsp;               "itemsPerPage": 25,

&nbsp;               "currentPage": 398,

&nbsp;               "pageCount": *Page number*

&nbsp;           },

&nbsp;           "list": \[

&nbsp;		.......





An example player return statement would look like looks like

{

&nbsp;                   "currentOrganization": {

&nbsp;                       "key": 13989,

&nbsp;                       "fullName": "Blue Springs South Jaguars",

&nbsp;                       "name": "Blue Springs South Jaguars",

&nbsp;                       "mascot": "Jaguars",

&nbsp;                       "abbreviation": "BSSHS",

&nbsp;                       "assetUrl": "https://on3static.com/uploads/assets/678/350/350678.png",

&nbsp;                       "asset": {

&nbsp;                           "key": 350678,

&nbsp;                           "domainOverride": null,

&nbsp;                           "domain": "on3static.com",

&nbsp;                           "sourceOverride": null,

&nbsp;                           "source": "/uploads/assets/678/350/350678.png",

&nbsp;                           "title": "team image",

&nbsp;                           "description": null,

&nbsp;                           "caption": null,

&nbsp;                           "category": null,

&nbsp;                           "altText": null,

&nbsp;                           "height": 538,

&nbsp;                           "width": 589,

&nbsp;                           "assetType": "Image",

&nbsp;                           "fileSystem": "s3",

&nbsp;                           "path": "/uploads/assets/678/350",

&nbsp;                           "type": "png",

&nbsp;                           "thumbnail": null,

&nbsp;                           "duration": 0,

&nbsp;                           "mimeType": "image/png"

&nbsp;                       },

&nbsp;                       "slug": "blue-springs-south-blue-springs-mo",

&nbsp;                       "primaryColor": "#144894"

&nbsp;                   },

&nbsp;                   "organizationLevel": "HighSchool",

&nbsp;                   "division": "HighSchool",

&nbsp;                   "hometown": {

&nbsp;                       "key": 24672,

&nbsp;                       "name": "Kansas City",

&nbsp;                       "state": {

&nbsp;                           "key": 26,

&nbsp;                           "name": "Missouri",

&nbsp;                           "abbreviation": "MO",

&nbsp;                           "countryKey": 1

&nbsp;                       },

&nbsp;                       "country": {

&nbsp;                           "key": 1,

&nbsp;                           "name": "United States",

&nbsp;                           "abbreviation": "US"

&nbsp;                       }

&nbsp;                   },

&nbsp;                   "hometownLatLong": "39.105754,-94.593335",

&nbsp;                   "position": {

&nbsp;                       "key": 7,

&nbsp;                       "name": "Edge",

&nbsp;                       "abbreviation": "EDGE",

&nbsp;                       "sportKey": 1,

&nbsp;                       "sport": {

&nbsp;                           "key": 1,

&nbsp;                           "name": "Football",

&nbsp;                           "slug": "football",

&nbsp;                           "abbreviation": "FB",

&nbsp;                           "isRankable": true,

&nbsp;                           "isIndustryRankable": true

&nbsp;                       },

&nbsp;                       "positionType": "Player"

&nbsp;                   },

&nbsp;                   "firstName": "Prince",

&nbsp;                   "lastName": "Goldsby",

&nbsp;                   "goesBy": null,

&nbsp;                   "dateOfBirth": null,

&nbsp;                   "sport": {

&nbsp;                       "key": 1,

&nbsp;                       "name": "Football",

&nbsp;                       "slug": "football",

&nbsp;                       "abbreviation": "FB",

&nbsp;                       "isRankable": true,

&nbsp;                       "isIndustryRankable": true

&nbsp;                   },

&nbsp;                   "status": {

&nbsp;                       "type": "None",

&nbsp;                       "shortTermSignee": false,

&nbsp;                       "date": null,

&nbsp;                       "committedAsset": null,

&nbsp;                       "committedAssetRes": null,

&nbsp;                       "transferredAsset": null,

&nbsp;                       "transferredAssetRes": null,

&nbsp;                       "committedOrganization": null,

&nbsp;                       "classRank": null,

&nbsp;                       "transferEntered": null,

&nbsp;                       "recruitmentYear": 2027,

&nbsp;                       "decommittedAsset": null,

&nbsp;                       "transfer": false,

&nbsp;                       "expectedToTransfer": false,

&nbsp;                       "recruitmentKey": 0,

&nbsp;                       "withdrawnTransfer": false,

&nbsp;                       "withdrawnTransferDate": null

&nbsp;                   },

&nbsp;                   "positionTypes": \[

&nbsp;                       "Player"

&nbsp;                   ],

&nbsp;                   "articleTaggingEnabled": true,

&nbsp;                   "officialVisits": \[],

&nbsp;                   "nilValuation": 0,

&nbsp;                   "isDraftPick": false,

&nbsp;                   "collegeName": null,

&nbsp;                   "college": null,

&nbsp;                   "recruitmentInterests": \[

&nbsp;                       {

&nbsp;                           "key": 889512,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 17525,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": 135474,

&nbsp;                           "secondaryPersonKey": 175553,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 889513,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 8288,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": false,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 889514,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 7576,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": false,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 889515,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 7578,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": false,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 891553,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 8158,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": 134729,

&nbsp;                           "secondaryPersonKey": 77045,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 891563,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 17543,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 893833,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 10166,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 893835,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 16674,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 895247,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 1867,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": 23136,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       },

&nbsp;                       {

&nbsp;                           "key": 908214,

&nbsp;                           "personSportKey": null,

&nbsp;                           "recruitmentKey": 257765,

&nbsp;                           "organizationKey": 5667,

&nbsp;                           "positionKey": 7,

&nbsp;                           "year": 2027,

&nbsp;                           "offer": true,

&nbsp;                           "contacted": false,

&nbsp;                           "organizationInterestLevel": 1,

&nbsp;                           "primaryPersonKey": null,

&nbsp;                           "secondaryPersonKey": null,

&nbsp;                           "status": "None",

&nbsp;                           "latestEventKey": null

&nbsp;                       }

&nbsp;                   ],

&nbsp;                   "personSportOrganizations": \[

&nbsp;                       {

&nbsp;                           "key": 862288,

&nbsp;                           "year": 2025,

&nbsp;                           "classYear": "Junior",

&nbsp;                           "organizationKey": 13989

&nbsp;                       }

&nbsp;                   ],

&nbsp;                   "tier": "Base",

&nbsp;                   "defaultSport": null,

&nbsp;                   "rating": null,

&nbsp;                   "predictions": null,

&nbsp;                   "key": 281494,

&nbsp;                   "name": "Prince Goldsby",

&nbsp;                   "slug": "prince-goldsby-281494",

&nbsp;                   "highSchoolName": "Blue Springs South",

&nbsp;                   "highSchool": {

&nbsp;                       "key": 13989,

&nbsp;                       "fullName": "Blue Springs South Jaguars",

&nbsp;                       "name": "Blue Springs South",

&nbsp;                       "knownAs": null,

&nbsp;                       "mascot": "Jaguars",

&nbsp;                       "abbreviation": "BSSHS",

&nbsp;                       "assetUrl": "https://on3static.com/uploads/assets/678/350/350678.png",

&nbsp;                       "defaultAsset": {

&nbsp;                           "key": 350678,

&nbsp;                           "domainOverride": null,

&nbsp;                           "domain": "on3static.com",

&nbsp;                           "sourceOverride": null,

&nbsp;                           "source": "/uploads/assets/678/350/350678.png",

&nbsp;                           "title": "team image",

&nbsp;                           "description": null,

&nbsp;                           "caption": null,

&nbsp;                           "category": null,

&nbsp;                           "altText": null,

&nbsp;                           "height": 538,

&nbsp;                           "width": 589,

&nbsp;                           "assetType": "Image",

&nbsp;                           "fileSystem": "s3",

&nbsp;                           "path": "/uploads/assets/678/350",

&nbsp;                           "type": "png",

&nbsp;                           "thumbnail": null,

&nbsp;                           "duration": 0,

&nbsp;                           "mimeType": "image/png"

&nbsp;                       },

&nbsp;                       "slug": "blue-springs-south-blue-springs-mo",

&nbsp;                       "primaryColor": "#144894",

&nbsp;                       "orgType": "HighSchool",

&nbsp;                       "orgTypeEnum": "HighSchool",

&nbsp;                       "division": null,

&nbsp;                       "siteKeys": null,

&nbsp;                       "urlSlug": "blue-springs-south-blue-springs-mo-13989"

&nbsp;                   },

&nbsp;                   "homeTownName": "Kansas City, MO",

&nbsp;                   "defaultAssetUrl": "https://on3static.com/uploads/assets/216/524/524216.png",

&nbsp;                   "defaultAsset": {

&nbsp;                       "key": 524216,

&nbsp;                       "domainOverride": null,

&nbsp;                       "domain": "on3static.com",

&nbsp;                       "sourceOverride": null,

&nbsp;                       "source": "/uploads/assets/216/524/524216.png",

&nbsp;                       "title": "player headshot",

&nbsp;                       "description": null,

&nbsp;                       "caption": null,

&nbsp;                       "category": null,

&nbsp;                       "altText": null,

&nbsp;                       "height": 136,

&nbsp;                       "width": 112,

&nbsp;                       "assetType": "Image",

&nbsp;                       "fileSystem": "s3",

&nbsp;                       "path": "/uploads/assets/216/524",

&nbsp;                       "type": "png",

&nbsp;                       "thumbnail": null,

&nbsp;                       "duration": 0,

&nbsp;                       "mimeType": "image/png"

&nbsp;                   },

&nbsp;                   "earlySignee": false,

&nbsp;                   "earlyEnrollee": false,

&nbsp;                   "positionAbbreviation": "EDGE",

&nbsp;                   "height": 76,

&nbsp;                   "formattedHeight": "6-4",

&nbsp;                   "weight": 210,

&nbsp;                   "classYear": 2027,

&nbsp;                   "athleteVerified": false,

&nbsp;                   "prospectVerified": false,

&nbsp;                   "classRank": "",

&nbsp;                   "recruitmentKey": 257765,

&nbsp;                   "age": null

&nbsp;               },


Then for the player get the id and then using the same session cookie BS we do this
https://www.on3.com/\_next/data/9o6Y-zkZonM\_NPn26kr95/rivals/langston-abernathy-242576.json?id=langston-abernathy-242

I guess for some reason the 9o6Y-zkZonM\_NPn26kr95 thing is just kinda there for some reason but hey whatever. Ill just uses this URL to get data from the places. the schools he has offered I can reference would be siteURLs



**247 SPORTS**


The URL looks like https://247sports.com/season/2027-football/recruits.json

A little more complicated since I cant get straight offer data from them I need to find out where that is in the website.

For getting the offer timelines I would probably need to get this example url using the ID. With they number after his naim being the key or just copying straight from the URL section to find the time line. From there im gonna need to do some webscrapping by first downloading each HTML file then sending that file to imidiently get deleted after so many iterations as to not slow things down as soon as data is gathered. 

https://247sports.com/Player/john-meredith-iii-46150593/TimelineEvents/

Example player
"Key": 174755,

&nbsp;       "Player": {

&nbsp;           "Key": 46150593,

&nbsp;           "Hometown": {

&nbsp;               "State": "Texas",

&nbsp;               "City": "Fort Worth"

&nbsp;           },

&nbsp;           "FirstName": "John",

&nbsp;           "LastName": "Meredith III",

&nbsp;           "FullName": "John Meredith III",

&nbsp;           "Height": "6-2",

&nbsp;           "Weight": 175.00,

&nbsp;           "Bio": "Transferred to North Crowley ahead of senior season. Previously attended Euless Trinity.\\r\\nAlso competes in track and field.\\r\\n-----\\r\\nTRACK \& FIELD\\r\\nTwice ran a 21.74 200-meter rep as a sophomore. Also triple jumped 43-5, per MileSplit.\\r\\nRecorded a 44-1.5 triple jump as a freshman in Spring 2024.\\r\\n- Gabe Brooks",

&nbsp;           "ScoutEvaluation": null,

&nbsp;           "Birthdate": "7/9/2008 12:00:00 AM",

&nbsp;           "ModifiedUser": "ChanceLinton",

&nbsp;           "ModifiedDate": "1/7/2026 7:02:54 PM",

&nbsp;           "CBSKey": 0,

&nbsp;           "Url": "https://247sports.com/player/john-meredith-iii-46150593/",

&nbsp;           "PlayerHighSchool": {

&nbsp;               "Name": "North Crowley"

&nbsp;           },

&nbsp;           "LastRecruitmentPlayerInstitution": 316239,

&nbsp;           "CurrentPlayerInstitution": 316239,

&nbsp;           "TwitterContact": null,

&nbsp;           "MobilePhoneContact": null,

&nbsp;           "PrimaryPlayerSport": 326370,

&nbsp;           "PrimaryPlayerPosition": {

&nbsp;               "Abbreviation": "CB"

&nbsp;           },

&nbsp;           "PrimaryRecruitment": null,

&nbsp;           "DefaultName": "John Meredith III",

&nbsp;           "DefaultAsset": 13520592,

&nbsp;           "DefaultAssetUrl": "https://s3media.247sports.com/Uploads/Assets/592/520/13520592.jpg",

&nbsp;           "HeroAsset": null,

&nbsp;           "QuoteAsset": null,

&nbsp;           "User": null,

&nbsp;           "ProStatPlayer": null,

&nbsp;           "CollegeStatPlayer": null,

&nbsp;           "BioOrDefault": "Transferred to North Crowley ahead of senior season. Previously attended Euless Trinity.\\r\\nAlso competes in track and field.\\r\\n-----\\r\\nTRACK \& FIELD\\r\\nTwice ran a 21.74 200-meter rep as a sophomore. Also triple jumped 43-5, per MileSplit.\\r\\nRecorded a 44-1.5 triple jump as a freshman in Spring 2024.\\r\\n- Gabe Brooks",

&nbsp;           "Rating": 98,

&nbsp;           "StarRating": 5,

&nbsp;           "NationalRank": 6,

&nbsp;           "PositionRank": 1,

&nbsp;           "StateRank": 1

&nbsp;       },

&nbsp;       "PlayerInstitution": 316239,

&nbsp;       "Year": 2027,

&nbsp;       "AnnouncementDate": null,

&nbsp;       "SignedInstitution": null,

&nbsp;       "Position": 24,

&nbsp;       "Institution": 20841,

&nbsp;       "State": 9,

&nbsp;       "PlayerSport": 326370,

&nbsp;       "CompositeStrength": "3",

&nbsp;       "FinalChoice": null,

&nbsp;       "HighestRecruitInterestEventType": "Offer",

&nbsp;       "HighestRecruitInterestEvent": 404055,

&nbsp;       "CommittedRecruitInterest": null,

&nbsp;       "CommittedInstitution": null,

&nbsp;       "HighestRecruitInterest": 921388,

&nbsp;       "PrimaryPlayerPosition": 350221,

&nbsp;       "PrimaryPosition": 24,

&nbsp;       "DefaultName": "John Meredith III",

&nbsp;       "CommitedInstitutionTeamImage": null,

&nbsp;       "RecruitInterestCount": 41,

&nbsp;       "RecruitInterestsUrl": "https://247sports.com/recruitment/john-meredith-iii-174755/recruitinterests/"

&nbsp;   },









