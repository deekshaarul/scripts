#!/usr/sup/gnu/bin/perl  
use feature qw(switch);

print "Choose the commands:\n1. Open a window\n2. Open Gmail\n3. Open a file from any directory\nChoice: ";

$ch = <STDIN>;
given ($ch) {
   when (1) {
        print "\nFolder to open with path: ";
        $a = <STDIN>;
        $a = 'nautilus '.$a;
        system($a);
   }
    when (2) {
        system('firefox https://mail.google.com');
   }
    when (3) {
        print "File to find : ";
        $a = <STDIN>;
        $a = 'locate -i '.$a;
        my $output = qx($a);
        
        open my $OUTPUT, '>', 'output.txt' or die "Couldn't open output.txt: $!\n";
        print $OUTPUT $output;
        close $OUTPUT;
        
        $c=1;
        foreach my $line (split /[\r\n]+/, $output) {
            print $c.". ".$line."\n";
            $c++;
        }
        print "Which line to open: ";
        $ans = <STDIN>;
        $c=1;
        foreach my $line (split /[\r\n]+/, $output) {
            if($ans == $c){
                $a='subl '.$line;
                system($a);
            }
            $c++;
        }
    }


   default {
       print "More commands shall be added";
   }
}



