# Photoshot - Photography Agency Website

## Overview
A static photography agency website built with HTML, CSS, and JavaScript, using Supabase as the backend for services, gallery, contacts, and authentication.

## Project Architecture
- **Type**: Static website (HTML/CSS/JS) with Supabase backend
- **Server**: Python `http.server` on port 5000 (serves static files with no-cache headers)
- **Backend**: Supabase (external) - configured in `js/config.js`
- **Frontend Framework**: Bootstrap 5, Swiper.js, Ionicons
- **No build step required**

## File Structure
```
├── index.html              # Main website page
├── server.py               # Python static file server (port 5000)
├── style.css               # Main stylesheet
├── admin/
│   ├── index.html          # Admin login page
│   ├── dashboard.html      # Admin dashboard
│   ├── admin-auth.js       # Authentication logic
│   └── admin-dashboard.js  # Dashboard functionality
├── js/
│   ├── config.js           # Supabase configuration (URL + anon key)
│   ├── supabase.js         # Supabase service functions
│   └── main.js             # Main website JavaScript
├── css/
│   └── vendor.css          # Third-party CSS
└── images/                 # Static images
```

## Running the Project
- Workflow "Start application" runs `python server.py` on port 5000
- The server serves all static files from the project root

## Supabase Configuration
- URL and anon key are stored in `js/config.js`
- Tables: services, gallery, contacts
- Storage bucket: images
- Auth: Email-based authentication for admin panel

## Recent Changes
- 2026-02-22: Initial Replit setup - added Python static file server and workflow
