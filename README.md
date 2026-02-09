## **Azure OIDC Configuration**

* OIDC integration in the JFrog Platform allows you to use services such as Azure DevOps with OpenID Connect to work on the JFrog Platform. With OIDC integration, you can allow the Azure DevOps CI pipelines to download and publish artifacts without storing JFrog passwords, tokens, or API keys in Azure.  
* Reference Link:   
  * JFROG Documentation: [JFrog Azure DevOps Extension](https://jfrog.com/help/r/jfrog-integrations-documentation/jfrog-azure-devops-extension)   
  * Azure Documentation: [jfrog-azure-devops-extension](https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file#using-openid-connect-oidc-authentication)

### **Install JFROG Azure DevOps Extension** 

* **Action to be performed by the Azure Organization Administrator**  
* Link: [https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?ta](https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file#Download-and-Installation)[https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file\#using-openid-connect-oidc-authentication](https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file#using-openid-connect-oidc-authentication)[b=readme-ov-file\#Download-and-Installation](https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file#Download-and-Installation)

### **Configuring OIDC Configuration in JFROG Platform** 

* **Action to be performed by JFROG Platform Administrator**  
* Link: [https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file\#using-openid-connect-oidc-authentication](https://github.com/jfrog/jfrog-azure-devops-extension/tree/v2?tab=readme-ov-file#using-openid-connect-oidc-authentication)

### **Add JFrog Service Connection in ADO** 

* **Action to be performed by Azure Project Administrator**  
* Go to the Azure Project  
* Click on “Project Settings.”  
* Under Pipelines \-\> Service Connections  
* Click on the  “New Service Connection” button  
* Select “Platform Version V2”
* Click on “Next.”  
* Fill the fields as shown below

**Note: In the above screenshot, change the “OpenID Connection provider name” and “Service Connection Name** 

### **Create Identity Mapping in Project OIDC Configuration** {#create-identity-mapping-in-project-oidc-configuration}

* **Action to be performed by:** Project Admin  
  * This step is required for workflows based on OIDC authentication  
  * Steps:  
    * Select the project from the project list for which “Identity Mapping” has to be configured  
    * Go to Administration \> General Management \> Manage Integrations  
    * Navigate to Identity Provider Configuration in Artifactory, which is configured by the Platform Admin  
      * Eg: myazureoidc  
    * Click on the “Add Identity Mapping” button  
    * Define Identity Mappings  
      * Claims JSON (Example):  
      * The below claim ensures all repos under the Azure organization can authenticate.

```
{ 
  "aud": "api://AzureADTokenExchange"
}
```

## **Sample Azure DevOps pipelines** 

### **Azure DevOps Pipeline Changes** 

* **Sample Azure DevOps Pipeline with OIDC configuration:**  
  * Reference Link:   
    * https://github.com/gnaga/pythonappADO
    * https://github.com/gnaga/pythonappADO/blob/main/azure-pipelines.yaml

**Below are the steps in the pipeline.**
```
    # Step 1: Authenticate with JFrog via OIDC  
    # Step 2: Get Python Version using task or Activate Python Virtual Environment and Install Build Tools  
    # Step 3: Install dependencies via JFrog CLI (pulls from nd-python)  
    # Step 4: Run Jfrog Curation Audit check  
    # Step 5: Download and Run Frogbot  
    # Step 6: Build Python wheel  
    # Step 7: Upload wheel to nd-python repo via JFrog CLI  
    # Step 8: Publish build info to JFrog  
    # Step 9: Publish wheel as pipeline artifact (for traceability)  
    # Step 10: Docker login to JFrog  
    # Step 11: Build Docker image with the wheel package  
    # Step 12: Push Docker image to JFrog Artifactory  
    # Step 13: Print deployment summary  
```

