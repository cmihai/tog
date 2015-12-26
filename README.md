# tog

Prepend current time to each line read from standard input.

There are plenty of packages that do it, but this one is mine. :)

## Usage

Usage: tog [OPTIONS]

Options:  
  --us    Show time with microsecond precision.  
  --help  Show this message and exit.  

## Example

    $ curl -v http://yahoo.com 2>&1 | tog --us

    [2015-12-26 16:07:39.616428] * Rebuilt URL to: http://yahoo.com/
    [2015-12-26 16:07:39.616428] * timeout on name lookup is not supported
    [2015-12-26 16:07:39.616428] *   Trying 2001:4998:44:204::a7...
    [2015-12-26 16:07:39.616428]   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    [2015-12-26 16:07:39.617406]                                  Dload  Upload   Total   Spent    Left  Speed
    [2015-12-26 16:07:39.617406] 
    [2015-12-26 16:07:39.784824]   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Connected to yahoo.com (2001:4998:44:204::a7) port 80 (#0)
    [2015-12-26 16:07:39.785742] > GET / HTTP/1.1
    ...
