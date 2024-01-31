const express = require('express');
const mongoose = require('mongoose');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const session = require('express-session');
const bcrypt = require('bcrypt');
const User = require('./models/User');

const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/leittechnik', {
});

const db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
  console.log('\x1b[32m%s\x1b[0m', 'All systems are go!')
});

// Set up middleware
app.use(express.urlencoded({ extended: true }));
app.use(session({ secret: 'alQ07%qPy#@7', resave: true, saveUninitialized: true }));
app.use(passport.initialize());
app.use(passport.session());

// Set up Passport
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

// Middleware to check authentication status
function redirectToLoginIfNotLoggedIn(req, res, next) {
  if (!req.isAuthenticated()) {
    return res.redirect('/login');
  }
  return next();
}

// Use middleware for / route
app.get('/', redirectToLoginIfNotLoggedIn, (req, res) => {
  res.sendFile(__dirname + '/index.html');
});


app.use(express.static('public'));


// Login
app.post('/login', passport.authenticate('local', {
  failureRedirect: '/login-failure',
}), (req, res) => {
  // success is handeled explicitly here, won't work otherwise
  res.json({ success: true, message: 'Erfolgreich Angemeldet' });
});




app.get('/login-failure', (req, res) => {
  res.status(401).json({ success: false, message: 'Login fehlgeschlagen' });
});

// Logout
app.get('/logout', (req, res) => {
  req.logout((err) => {
    if (err) {
      return res.status(500).send("Error during logout");
    }
    res.redirect('/login');
  });
});

// Render login page
app.get('/login', (req, res) => {
  res.sendFile(__dirname + '/views/login.html');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running: http://localhost:${PORT}`);
});
