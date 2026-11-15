LAB 3 - MONITORING, LOGGING & DEVSECOPS
Student: Vishu
Roll Number: 2301730276

PACKAGE CONTENTS
- Reports/: seven corrected PDF reports.
- Section_1_Ansible through Section_6_FeatureFlags_Testing/: practical configuration/source files.
- Section_1...Section_6/Evidence/: screenshots relevant to each practical.
- screenshots/: master copy of all 17 supplied screenshots.
- Section_7_Final_Report/: pointer/readme for the consolidated report.

IMPORTANT PROVENANCE NOTE
The uploaded report-and-screenshot archive contained seven PDFs and 17 screenshots. The separate source-code ZIP from the earlier part of the conversation was not mounted in the current file-processing session. To avoid claiming that unavailable originals were copied, the configuration/source files in this package were reconstructed from the commands and configurations printed in the supplied PDFs and the work documented in the conversation. Review them against your original working folders before treating them as byte-for-byte originals.

Section 4 Jenkinsfile is a portable copy of the Jenkins pipeline shown in the report. The actual scan JSON was archived by Jenkins and was not included in the uploaded archive. The pipeline uses `|| true`, so a successful build does not prove there were no vulnerabilities.
The Terraform lock file is intentionally not fabricated; run `terraform init` in Section_2_Terraform to generate it for the local platform.
