import { LightningElement ,track} from 'lwc';
import validateStudent from '@salesforce/apex/LeaveRequestController.validateStudent';
import updateLeaveRequest from '@salesforce/apex/LeaveRequestController.updateLeaveRequest';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';

const columns = [
    {label:'Id' , fieldName:'Id'},
    {label:'From_Date__c', fieldName:'From_Date__c'},
    {label:'To_Date__c', fieldName:'To_Date__c'},
    {label:'Reason__c', fieldName:'Reason__c'},
    {label:'Head_Comment__c', fieldName:'Head_Comment__c'},
    {label:'Student__c', fieldName:'STUDENT__c'},
    { 
        label: 'Approval Status', 
        fieldName: 'Status__c', 
        type: 'text',
        cellAttributes: {
            class: { fieldName: 'statusColor' } ,
            alignment: 'left'
        } 
        
    },
    { 
        type: 'button', 
        label: 'Edit', 
        typeAttributes: {
            label: 'Edit',
            name: 'edit',
            variant: 'brand'
        }
    }
];

export default class MyLeaves extends LightningElement {
    
    @track username = '';
    @track password = '';
    @track data = [];
    @track isLoggedIn = false;
    @track error = '';
    columns = columns;
    @track isEditModalOpen = false;
    @track editRecord = {};

    handleUsernameChange(event){
        this.username = event.target.value;
    }
    handlePasswordChange(event){
        this.password = event.target.value;
    }

    async handleLogin() {
        this.error = '';
        this.data = [];

        if (!this.username || !this.password) {
            this.error = 'Please enter both username and password.';
            return;
        }

        try {
            const result = await validateStudent({ username: this.username, password: this.password });

            if (result.length > 0) {
                // this.data = [...result];

                this.data = result.map(row => ({
                ...row,
                statusColor: row.Status__c === 'Approved' ? 'slds-text-color_success' :
                             row.Status__c === 'Pending' ? 'slds-text-color_warning' :
                             'slds-text-color_error'
            }));


                this.isLoggedIn = true;
            } else {
                this.error = 'Invalid credentials or no leave requests found.';
            }
        } catch (error) {
            console.error(error);
            this.error = 'An error occurred while logging in.';
        }
    }
    handleLogout() {
        this.isLoggedIn = false;
        this.username = '';
        this.password = '';
        this.data = [];
    }

    handleRowAction(event) {
        const actionName = event.detail.action.name;
        const row = event.detail.row;

        if (actionName === 'edit') {
            this.editRecord = { ...row };
            this.isEditModalOpen = true;
        }
    }

    handleEditChange(event) {
        this.editRecord[event.target.dataset.field] = event.target.value;
    }

    async saveEdit() {
        try {
            await updateLeaveRequest({ leaveRequest: this.editRecord });

            this.data = this.data.map(item =>
                item.Id === this.editRecord.Id ? { ...this.editRecord } : item
            );

            this.dispatchEvent(
                new ShowToastEvent({
                    title: 'Success',
                    message: 'Record updated successfully!',
                    variant: 'success' 
                })
            );

            this.isEditModalOpen = false;
        } catch (error) {
            console.error('Error updating record:', error);
        }
    }

    closeEditModal() {
        this.isEditModalOpen = false;
    }

}