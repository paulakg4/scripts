function syncUSnewsletters()
{
  Logger.clear();
  var done = false;
//----Put your folder id's here-v
  var folders = ["0B5McCjQAGnGQUTR3N3hiZUNCeEk", "0B5McCjQAGnGQNzljZmMzNjgtZDg1Ni00MDg1LTkxZTYtOTlmN2EwY2JlNDA1", "0B5McCjQAGnGQYzc0YzNiNDgtYjk4ZC00YmVmLTk2MTQtYzVlNjdjYTVkNWVi", "0B5McCjQAGnGQMTk5ZjhlMDctMzU5Ni00MTliLWI3MTItOTM1MzJiM2RmYzQz", "0B5McCjQAGnGQNWYzMTdiYzAtOTFmNi00NzVlLThlY2UtNWU3MTFkOTk2YTNm"];
  

//---And the Google Sites 'List Page' here-V

  var page = SitesApp.getPageByUrl("https://sites.google.com/a/domainname/us-office/us-newsletters");
  
  while(!done){
    // The while loop and try - catch statement are used to automatically retry if there's an issue during the execution (common issue: SitesApp: Internal error).
    var oldlistItems = page.getListItems();
    for(i in oldlistItems){
      oldlistItems[i].deleteListItem();
    }
    for(i=0; i<folders.length; i++) {
        var files = DocsList.getFolderById(folders[i]).getFiles();
        var filelist = Array();
                for(j in files){
                        /*** Title field ***/
                        var title = "<a href=\""+files[j].getUrl()+"\">"+files[j].getName()+"</a>";
                        /*** Type field ***/
                        var type = files[j].getType();
                        // condition: if the type is "blob_item" replace it by the filename extension
                        if(type == "blob_item"){
                          type = files[j].getName().substring(files[j].getName().lastIndexOf('.'));
                        }
                        /*** Size field ***/
                        // To indicate the size properly, we need multiple conditions:
                        // - If size > 0, we show the size, else (if size = 0) it's a Google Docs file and we can hide this zero.
                        // - Calculate the length of the number (28099 is five digits, 2158080 is seven digits):
                        // If length < 7 digits then size is < 1mb. Indicate "kb" and remove the last digits (the bytes).
                        // Else, indicate "mb" and remove the last digits (kilobytes and bytes).
                        var size = files[j].getSize();
                        if(size > 0){
                          var length = size.toString().length;
                          if(length < 7){
                            size = size.toString().substring(0,length - 3) + "kb";
                          }
                          else{
                            size = size.toString().substring(0,length - 6) + "mb";
                          }
                        }
                        else{
                          size = '';
                        }
                        /*** Owner field ***/
                        // Take the email address and remove everything after the @.
                        var owner = files[j].getOwner().toString().substring(0,files[j].getOwner().toString().indexOf('@'));
                        /*** Last Updated field ***/
                        // .formatDate() is a method from the Utilities Services
                        var lastUpdated = Utilities.formatDate(files[j].getLastUpdated(), "GMT", "yyyy-MM-dd");
                        var lenlastUpdated = lastUpdated.toString().length;
                        if(lenlastUpdated < 3) {
                          var lastUpdated = Utilities.formatDate(Date.today(), "GMT", "yyyy-MM-dd");
                        }
                        
                        /***
                        


                Add data according to the order of columns in your list        
                        
                        
                        ***/
                        var addfile = ([title, type]); //Ive ommited these values: lastUpdated, owner
                        
                        filelist.push(addfile);
                }
         try{    
               for(entry in filelist) {
                 title = (filelist[entry][0]);
                 lastUpdated = filelist[entry][1];
                 
                 page.addListItem([title, lastUpdated]);
               }
              
         }catch(e){
                 Logger.log(e)
               }
      done = true;
    }
  }
}

