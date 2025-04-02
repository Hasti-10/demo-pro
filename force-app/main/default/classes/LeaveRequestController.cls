public with sharing class LeaveRequestController {
    
    @AuraEnabled(cacheable=true)
      public static List<Leave_Request__c> validateStudent(String username, String password) {
          List<Student__c> students = [
              SELECT Id, Password__c FROM STUDENT__c 
              WHERE Username__c = :username 
              LIMIT 1
          ];
         
          if (students.isEmpty()) {
              return new List<Leave_Request__c>();
          }
          
          STUDENT__c student = students[0];
          if (student.Password__c != password) {
            return new List<Leave_Request__c>(); // Incorrect password
        }
  
        List<Leave_Request__c> data = [
            SELECT Id, From_Date__c, To_Date__c, Reason__c, Head_Comment__c,STUDENT__c,Status__c
            FROM Leave_Request__c 
            WHERE Student__c = :student.Id
         ];

         return data;

      }

      @AuraEnabled
    public static void updateLeaveRequest(Leave_Request__c leaveRequest) {
        update leaveRequest;
    }
  }
  