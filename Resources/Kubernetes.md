# Kubernetes

A list of vetted sources for attacking and securing Kubernetes

## General

* [Kubernetes Docs](https://kubernetes.io/docs/home/) - Kubernetes
* [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/) - Kubernetes
* [Kube By Example](https://kubebyexample.com/) - RedHat
* [The Illustrated Children's Guide to Kubernetes](https://youtu.be/4ht22ReBjno) - Matt Butcher
* [Kubernetes Failure Stories](https://k8s.af/) - @try_except_
* [Kubernetes: The Documentary - Part 1](https://www.youtube.com/watch?v=BE77h7dmoQU) - Honeypot
* [Kubernetes: The Documentary - Part 2](https://www.youtube.com/watch?v=318elIq37PE) - Honeypot
* [The Kubernetes Networking Guide](https://www.tkng.io/) - networkop

## Tools
* [KIND](https://kind.sigs.k8s.io/) - KIND
* [K3s](https://k3s.io/) - K3s

## Vulnerabilities
* [Official CVE Feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/) - Kubernetes
* [Github - Kubernetes - Issues (open security bugs)](https://github.com/kubernetes/kubernetes/issues?q=state%3Aopen%20label%3A%22area%2Fsecurity%22%20AND%20label%3Akind%2Fbug) - Kubernetes
* [CVE Details for Kubernetes](https://www.cvedetails.com/vulnerability-list/vendor_id-15867/product_id-34016/Kubernetes-Kubernetes.html) - CVE Details

## Securing Kubernetes

* [Kubernetes - Security Audits](https://github.com/kubernetes/community/tree/master/sig-security) - Kubernetes (sig-security)
* [Containers Matrix](https://attack.mitre.org/matrices/enterprise/containers/) - Mitre
* [11 Ways (Not) to Get Hacked](https://kubernetes.io/blog/2018/07/18/11-ways-not-to-get-hacked/) - Andrew Martin (Kubernetes)
* [Kubernetes Security Best Practices](https://youtu.be/wqsUfvRyYpw) - Ian Lewis, (Google)
* [10 Kubernetes Security Context settings you should understand](https://snyk.io/blog/10-kubernetes-security-context-settings-you-should-understand/) - Eric Smalling, Matt Jarvis (Snyk)
* [Threat matrix for Kubernetes](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/) - Yossi Weizman (Microsoft)
    * [Secure containerized environments with updated threat matrix for Kubernetes](https://www.microsoft.com/en-us/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes/) - Yossi Weizman (Microsoft)
    * [Threat Matrix for Kubernetes - Matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
* [Protecting Yourself with Pod Security Policies](https://starkandwayne.com/blog/protecting-yourself-with-pod-security-policies/) - James Hunt
* [Kubernetes Built-in Controls Workshop](https://securek8s.dev/) - Connor Gilbert (StackRox)
* [Top 10 Kubernetes Application Security Hardening Techniques](https://blog.aquasec.com/kubernetes-hardening-techniques) - Rory McCune (Aquasec)
* [How to secure your Kubernetes control plane and node components](https://www.cncf.io/blog/2021/08/20/how-to-secure-your-kubernetes-control-plane-and-node-components/) - Amit Ashwini Bhagat (LOGIQ.AI)
* [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF) - NSA
* [OWASP Kubernetes Top Ten](https://owasp.org/www-project-kubernetes-top-ten/) - OWASP
* [Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html) - OWASP

## Attacking Kubernetes

### General

* [KubeCon NA 2019 CTF](https://securekubernetes.com/) - securekubernetes
  * [Kubecon video NA 2019 CTF](https://youtu.be/UdMFTdeAL1s)
* [Kubernetes Pentest Methodology Part 1](https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-1) - Or Ida (CyberArk)
* [Kubernetes Pentest Methodology Part 2](https://www.cyberark.com/resources/conjur-secrets-manager-enterprise/kubernetes-pentest-methodology-part-2) - Or Ida (CyberArk)
* [Kubernetes Pentest Methodology Part 3](https://www.cyberark.com/resources/conjur-secrets-manager-enterprise/kubernetes-pentest-methodology-part-3) - Or Ida (CyberArk)
* [Using Kubelet Client to Attack the Kubernetes Cluster](https://www.cyberark.com/resources/secure-devops-pipelines-and-cloud-native-apps/using-kubelet-client-to-attack-the-kubernetes-cluster) - Eviatar Gerzi (Cyber Ark)
* [The Path Less Traveled: Abusing Kubernetes Defaults](https://youtu.be/HmoVSmTIOxM) - Ian Coldwater & Duffie Cooley
  * [Github repo for demos](https://github.com/mauilion/blackhat-2019) - Ian Coldwater & Duffie Cooley
* [Advanced Persistence Threats: The Future of Kubernetes Attacks](https://youtu.be/auUgVullAWM) - Ian Coldwater & Brad Geesaman
* [Hacking and Hardening Kubernetes Clusters by Example](https://youtu.be/vTgQLzeBfRU) - Brad Geesaman (Symantec)
* [Creating a Super-privileged Pod with Root and Host Namespaces](https://downey.io/notes/dev/kubernetes-privileged-root-pod-example) - Tim Downey
* [Command and KubeCTL - Real-World Kubernetes Security for Pentesters](https://www.youtube.com/watch?v=cRbHILH4f0A) - Mark Maning (NCC Group)
  * [Slides](https://docs.google.com/presentation/d/1y6KGGT5Uw27cCgFMKiGv0NjRhq8YvjY_S9UG8s_TThg)
* [Kubenomicon](https://kubenomicon.com/Kubenomicon.html) - Graham Helton (Kubenomicon)
* [Stratus Red Team - Kubernetes](https://stratus-red-team.cloud/attack-techniques/kubernetes/) - Stratus Red Team
* [HatTricks CLoud - Kubernetes Pentesting](https://cloud.hacktricks.xyz/pentesting-cloud/kubernetes-security) - Hatricks.xyz

### Labs
* [DEF CON Safe Mode Red Team Village - Madhu Akula - Kubernetes Goat Vulnerable by Design](https://youtu.be/aEaSZJRbnTo) - Madhu Akula
    * [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) - Madhu Akula
* [Bust-a-Kube](https://www.bustakube.com/) - Jay Beale
   * [Attacking and Defending Kubernetes: Bust-A-Kube – Episode 1](https://www.inguardians.com/blog/attacking-and-defending-kubernetes-bust-a-kube-episode-1/) - Jay Beale (InGuardians)
   * [Kubernetes Hacking and Hardening Episode 2: Bust a Kube (Part of the BeyondTrust webinar series)](https://www.beyondtrust.com/resources/webinars/kubernetes-hacking-and-hardening-episode-2-bust-a-kube) - Jay Beale (InGuardians)

### Initial Access
* [Making Sense of Kubernetes Initial Access Vectors Part 1 – Control Plane](https://www.wiz.io/blog/making-sense-of-kubernetes-initial-access-vectors-part-1-control-plane) - Shay Berkovich (Wiz.io)
* [Making Sense of Kubernetes Initial Access Vectors Part 2 - Data Plane](https://www.wiz.io/blog/kubernetes-data-plane) - Shay Berkovich (Wiz.io)

### Privilege Escalation
* [Climbing The Ladder | Kubernetes Privilege Escalation (Part 1)](https://www.sentinelone.com/blog/climbing-the-ladder-kubernetes-privilege-escalation-part-1/) - Shaul Ben Hai (Sentinel One)
* [Climbing The Ladder | Kubernetes Privilege Escalation (Part 2)](https://www.sentinelone.com/blog/climbing-the-ladder-kubernetes-privilege-escalation-part-2/) - Shaul Ben Hai (Sentinel One)
* [Privileged pod escalations in Kubernetes and GKE](https://security.googleblog.com/2022/05/privileged-pod-escalations-in.html) - GKE and Anthos Platform Security Teams

## Threat Research
* [Analyzing Activity on Kubernetes Ports: Potential Backdooring Through the Kubelet API](https://blog.rapid7.com/2018/06/27/analyzing-the-kubernetes-hack-backdooring-through-the-kubelet-api/) - Shan Sikdar (Rapid7)
* [Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances](https://unit42.paloaltonetworks.com/azure-container-instances/) - Yuval Avrahami (Unit 42)
* [Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms](https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/) - Yuval Avrahami (Unit 42)
* [Dirty DAG: New Vulnerabilities in Azure Data Factory’s Apache Airflow Integration](https://unit42.paloaltonetworks.com/azure-data-factory-apache-airflow-vulnerabilities/) - Ofir Balassiano & David Orlovsky (Unit 42)

## Open Source Tools

* [Kubernetes Python Client](https://github.com/kubernetes-client/python) - Kubernetes
* [Kubernetes Go Client](https://github.com/kubernetes/client-go) - Kubernetes
* [Kube-Hunter](https://github.com/aquasecurity/kube-hunter) - Aquasec
* [Peirates](https://github.com/inguardians/peirates) - Inguardians
* [KubiScan](https://github.com/cyberark/KubiScan) - Eviatar Gerzi (CyberArk)
* [KubeAudit](https://github.com/Shopify/kubeaudit) - Shopify
* [Kube-Bench](https://github.com/aquasecurity/kube-bench) - Aquasec
* [KubeLinter](https://github.com/stackrox/kube-linter) - Stackrox
