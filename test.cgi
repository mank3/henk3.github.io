#!/usr/bin/perl -w

use strict;
use DBI;
use CGI qw(:standard);

my $dbh = DBI->connect(
	"DBI:mysql:database=restricted:host=localhost", 
	"rsh",
	"__DATABASE_PASSWORD__") or die "Database connection failed";

my $query = undef;
if(param("quote")) { 
	$query = "SELECT id, text FROM quotes WHERE id = " . $dbh->quote(param("quote"));
} else { $query = "SELECT id, text FROM quotes ORDER BY RAND() LIMIT 1"; }

my $sth = $dbh->prepare($query);
$sth->execute() or die "Query Failed";
my @result = $sth->fetchrow_array();

print header;
if(@result) {
	print "Quote #" . $result[0] . ": " . $result[1]
} else { print "Quote not found"; }
