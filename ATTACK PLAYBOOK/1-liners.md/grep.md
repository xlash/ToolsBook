# Find HTTP(s) in recursive files
grep -ERo 'http[s]?://[a-zA-Z.-\:0-9]*/[0-9a-zA-Z.-\/]*' *
