const supportOTO_link=document.querySelector('.menu--list .menu[data-type="CS"]');supportOTO_link&&document.querySelector('.menu--list .menu[data-type="CS"]').classList.add("oneToOne_link");const oneToOneLinks=document.querySelectorAll(".oneToOne_link");window.addEventListener("load",function(){if(oneToOneLinks.forEach(link=>{link.addEventListener("click",function(e){e.preventDefault(),callModal()})}),new URLSearchParams(window.location.search).get("oneToOneModal")==="true"){callModal();const newUrl=new URL(window.location.href);newUrl.searchParams.delete("oneToOneModal"),window.history.replaceState({},"",newUrl)}}),document.addEventListener("DOMContentLoaded",()=>{const prevAdditionalAction=sessionStorage.getItem("prev_additional_action"),saveModal=sessionStorage.getItem("oneToOneModal");prevAdditionalAction=="true"&&saveModal=="true"&&window.isLoggedIn&&(callModal(),sessionStorage.removeItem("prev_additional_action"),sessionStorage.removeItem("oneToOneModal"))});function callModal(){customerMd5Hash?openModalWithContent("1:1 \uBB38\uC758\uD558\uAE30",`
            <div class="inquiry-container" style="">
                <div class="inquiry-form" style="">
                    <div class="inquiry-textarea-wrapper" style="text-align:center;margin-bottom:20px">
                        <div style="margin-top:20px;">
                            <p class="body-2" style="color:var(--text-secondary, #434548);">\uC81C\uD488 \uAD00\uB828 \uC815\uBCF4\uC640 \uC790\uC8FC \uBB3B\uB294 \uC9C8\uBB38\uC744 \uD655\uC778\uD574 \uBCF4\uC138\uC694.</p>
                        </div>
                        <div style="margin-top:10px;display:flex;gap:32px;justify-content:center">
                            <span 
                                onclick="window.location.href='/blogs/product-faq'" 
                                style="
                                    color:var(--primary, #000);
                                    cursor:pointer;
                                    color:#0000FF;
                                    text-decoration-line: underline;
                                    text-decoration-color:#0000FF;">
                                \uC81C\uD488 FAQ
                            </span>
                            <span 
                                onclick="window.location.href='/blogs/service-faq-new'" 
                                style="
                                    color:var(--primary, #000);
                                    cursor:pointer;
                                    color:#0000FF;
                                    text-decoration-line: underline;
                                    text-decoration-color:#0000FF;">
                                \uC11C\uBE44\uC2A4 FAQ
                            </span>
                        </div>
                    </div>
                    <div class="form-header" style="">
                        <p class="body-2 form-group-label" style="">
                            \uBB38\uC758 \uC720\uD615
                            <span class="form-group-label-require" style="">*</span>
                        </p>
                        <select name="inquiry_type" class="inquiry_type" style="">
                            <option selected hidden disabled>\uBB38\uC758 \uC720\uD615\uC744 \uC120\uD0DD\uD558\uC138\uC694.</option>
                            <option value="\uC8FC\uBB38/\uACB0\uC81C">\uC8FC\uBB38/\uACB0\uC81C</option>
                            <option value="\uBC30\uC1A1">\uBC30\uC1A1</option>
                            <option value="\uB9E4\uC7A5">\uB9E4\uC7A5</option>
                            <option value="\uC81C\uC548/\uCE6D\uCC2C/\uBD88\uB9CC\uC871">\uC81C\uC548/\uCE6D\uCC2C/\uBD88\uB9CC\uC871</option>
                            <option value="\uCFE0\uD3F0/\uD61C\uD0DD/\uB9AC\uD37C\uB7F4">\uCFE0\uD3F0/\uD61C\uD0DD/\uB9AC\uD37C\uB7F4</option>
                            <option value="\uD488\uC9C8\uBCF4\uC99D/\uC815\uD488\uB4F1\uB85D">\uD488\uC9C8\uBCF4\uC99D/\uC815\uD488\uB4F1\uB85D</option>
                            <option value="\uAE30\uD0C0">\uAE30\uD0C0</option>
                            <option value="AS\uC2E0\uCCAD/\uBB38\uC758">AS\uC2E0\uCCAD/\uBB38\uC758</option>
                        </select>
                    </div>
                    
                    <div class="form-body" style="">
                        <div class="form-body-header" style="">
                            <div class="inquiry-title-div" style="">
                                <p class="body-2 inquiry-title-name" style="">
                                    \uC81C\uBAA9<span class="form-group-label-require">*</span>
                                </p>
                                <p class="body-3 inquiry-title-name_sub" style="">
                                    <span class="title-text_count">0</span>/<span>40</span>
                                </p>
                            </div>
                            <input type="text" placeholder="\uC81C\uBAA9\uC744 \uC785\uB825\uD558\uC138\uC694." name="title" id="" class="inquiry_title" style="">
                        </div>
                
                        <div class="inquiry-textarea-wrapper" style="">
                            <div class="inquiry-textarea-wrapper-title" style="">
                                <p class="body-2" style="">
                                    \uB0B4\uC6A9
                                    <span class="form-group-label-require">*</span>
                                </p>
                                <p class="body-3" style="">
                                    <span class="desc-text_count">0</span>/<span>2,000</span>
                                </p>
                            </div>
                            <textarea name="opinion" placeholder="\uC6B4\uC601\uC815\uCC45\uACFC \uB9DE\uC9C0 \uC54A\uB294 \uBE44\uBC29\uC131 \uAE00 / \uC695\uC124 \uB4F1\uC740 \uC0AD\uC81C\uB429\uB2C8\uB2E4. \uAC1C\uC778\uC815\uBCF4, \uACB0\uC81C\uC815\uBCF4\uB294 \uAE30\uC7AC \uBD88\uAC00\uD558\uBA70 \uC791\uC131 \uC2DC \uC784\uC758 \uC0AD\uC81C \uB420 \uC218 \uC788\uC2B5\uB2C8\uB2E4." class="inquiry_desc" id="" cols="30" rows="5" style=""></textarea>
                        </div>
                        
                        <div class="inquiry-media-wrapper" style="margin-bottom:40px">
                            <div class="inquiry-media-wrapper-title" style="">
                                <p class="body-2">\uC0AC\uC9C4/\uC601\uC0C1 \uCCA8\uBD80</p>
                                <div class="inquiry-media-wrapper-title-info">
                                    <p class="body-3" style="">*\uD30C\uC77C \uCD5C\uB300 \uC6A9\uB7C9 : \uC0AC\uC9C4 5MB, \uC601\uC0C1 10MB</p>
                                    <p class="body-3" style="">*\uCCA8\uBD80\uD30C\uC77C\uC758 \uC6A9\uB7C9\uC774 \uCD08\uACFC\uB420 \uACBD\uC6B0, \uAE00\uC774 \uB4F1\uB85D\uB418\uC9C0 \uC54A\uC2B5\uB2C8\uB2E4.</p>
                                </div>
                            </div>

                            <div class="inquiry-media-wrapper-content-wrapper" style="">
                                <div class="inquiry-media-input-wrapper">
                                    <input type="file" id="fileInput" accept="image/png, image/jpeg, image/jpg, image/gif, image/bmp, image/webp, video/mov, video/mp4" multiple style="">
                                    <label for="fileInput" style="">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
                                            <path d="M8 3V13" stroke="black" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"/>
                                            <path d="M3 8H13" stroke="black" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"/>
                                        </svg>
                                    </label>
                                </div>
                                <div id="preview" class="inquiry-media-preview-wrapper" style="">
                                    <!--\uBBF8\uB9AC\uBCF4\uAE30 -->
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="inquiry-bottom hidden" style="text-align:center">
                        <div style="margin-top:40px;">
                            <p class="body-2" style="color:var(--text-secondary, #434548);">AS\uC2E0\uCCAD \uBC0F \uBB38\uC758\uB294 \uCC57\uBD07 \uC0C1\uB2F4\uC744 \uD1B5\uD574\uC11C\uB9CC \uAC00\uB2A5\uD569\uB2C8\uB2E4.</p>
                            <p class="body-2" style="color:var(--text-secondary, #434548);">\uBE60\uB974\uACE0 \uC815\uD655\uD55C \uC815\uBCF4 \uD655\uC778\uACFC \uC6D0\uD65C\uD55C \uC0C1\uB2F4\uC744 \uC704\uD574</p>
                            <p class="body-2" style="color:var(--text-secondary, #434548);">\uC815\uD488\uB4F1\uB85D \uD6C4 \uC9C4\uD589\uD574 \uC8FC\uC138\uC694.</p>
                        </div>
                        <div style="margin-top:40px;">
                            <p class="body-2" style="color:var(--text-secondary, #434548);">
                                *\uC815\uD488\uB4F1\uB85D \uD6C4 \uC81C\uD488\uC5D0 \uD638\uD658\uB418\uB294 
                            <span 
                                onclick="window.location.href='/pages/easy-repair'" 
                                style="
                                    color:var(--primary, #000);
                                    cursor:pointer;
                                    color:#0000FF;
                                    text-decoration-line: underline;
                                    text-decoration-color:#0000FF;">
                                \uC774\uC9C0\uB9AC\uD398\uC5B4
                            </span>
                            \uB97C \uD655\uC778\uD574
                            </p>
                            <p class="body-2" style="color:var(--text-secondary, #434548);">
                            \uBD80\uD488\uC744 \uC27D\uACE0 \uAC04\uD3B8\uD558\uAC8C \uAD50\uCCB4\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4.
                            </p>
                        </div>
                        <div style="margin-top:40px;display:flex;flex-direction:column;gap:12px;">
                            <div style="display:flex;gap:12px;justify-content:center">
                                <p class="body-3" style="color:var(--text-tertiary, #7C8084);">\uC544\uC9C1 \uC815\uD488\uB4F1\uB85D\uC744 \uD558\uC9C0 \uC54A\uC73C\uC168\uB098\uC694?</p>
                                <div class="body-3 product-registration" style="padding-left:12px;color:var(--primary, #000);cursor:pointer;
                                color:#0000FF;
                                text-decoration-line: underline;
                                text-decoration-color:#0000FF;">\uC815\uD488\uB4F1\uB85D</div>
                            </div>
                            <div style="display:flex;gap:12px;justify-content:center">
                                <p class="body-3" style="color:var(--text-tertiary, #7C8084);">\uC774\uBBF8 \uC815\uD488\uB4F1\uB85D\uC744 \uD558\uC2E0 \uACE0\uAC1D\uB2D8</p>
                                <div class="body-3 chatbot-inquiry" style="padding-left:12px;color:var(--primary, #000);cursor:pointer;
                                color:#0000FF;
                                text-decoration-line: underline;
                                text-decoration-color:#0000FF;">\uCC57\uBD07\uBB38\uC758</div>
                            </div>
                        </div>
                    </div>
                </div>

            <div class="apply_btn_wrapper inquire">
                <button class="apply-ask_btn">
                    <p style="margin: 0;">\uBB38\uC758 \uB4F1\uB85D\uD558\uAE30</p>
                </button>
            </div>
        `,()=>{document.querySelector(".modal--contents").style.height="auto",document.querySelector(".modal--contents").style.marginBottom="50px";const fileInput=document.getElementById("fileInput"),preview=document.getElementById("preview"),asFormBody=document.querySelector(".inquiry-container .form-body"),asBtn=document.querySelector(".inquiry-bottom .product-registration"),chatbotBtn=document.querySelector(".inquiry-bottom .chatbot-inquiry"),asDesc=document.querySelector(".inquiry-bottom"),selectElement=document.querySelector(".inquiry_type");selectElement.addEventListener("change",()=>{selectElement.value==="\uBB38\uC758 \uC720\uD615\uC744 \uC120\uD0DD\uD558\uC138\uC694."?selectElement.style.color="#A4AAB0":(selectElement.style.color="#000",selectElement.value==="AS\uC2E0\uCCAD/\uBB38\uC758"?(asFormBody.classList.add("hidden"),asDesc.classList.remove("hidden")):(asFormBody.classList.remove("hidden"),asDesc.classList.add("hidden")))}),asBtn.addEventListener("click",()=>{customerMd5Hash?openProductRegisterModal():commonLoginModal("productRegisterModal")}),chatbotBtn.addEventListener("click",()=>{closeAlertModal(),window.open("https://letus-gptbot.bizmsg.io/gpt/SIDIZ_CHATBOT","\uC2DC\uB514\uC988 \uB300\uD654\uD615 AI \uCC57\uBD07","width=1000,height=800,top=200,left=200,resizable=no,scrollbars=yes")}),selectElement.value==="\uBB38\uC758 \uC720\uD615\uC744 \uC120\uD0DD\uD558\uC138\uC694."&&(selectElement.style.color="#A4AAB0");const MAX_FILES=5;let selectedFiles=[];const IMAGE_MAX_SIZE=5*1024*1024,VIDEO_MAX_SIZE=10*1024*1024,allowedExtensions=["png","jpeg","jpg","gif","bmp","webp","mp4","mov"];fileInput.addEventListener("change",function(event){const validFiles=Array.from(event.target.files).filter(file=>{const fileExtension=file.name.split(".").pop().toLowerCase();return allowedExtensions.includes(fileExtension)?file.type.startsWith("image/")&&file.size>IMAGE_MAX_SIZE?(showErrorModal("\uC774\uBBF8\uC9C0\uB294 \uCD5C\uB300 5MB\uAE4C\uC9C0 \uC5C5\uB85C\uB4DC\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4."),fileInput.value="",!1):file.type.startsWith("video/")&&file.size>VIDEO_MAX_SIZE?(showErrorModal("\uC601\uC0C1\uC740 \uCD5C\uB300 10MB\uAE4C\uC9C0 \uC5C5\uB85C\uB4DC\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4."),fileInput.value="",!1):!0:(showErrorModal("\uC9C0\uC6D0\uD558\uC9C0 \uC54A\uB294 \uD30C\uC77C \uD615\uC2DD\uC785\uB2C8\uB2E4."),fileInput.value="",!1)});if(selectedFiles.length+validFiles.length>MAX_FILES){showErrorModal(`\uCD5C\uB300 ${MAX_FILES}\uAC1C\uC758 \uD30C\uC77C\uB9CC \uC5C5\uB85C\uB4DC\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4.`),fileInput.value="";return}selectedFiles=selectedFiles.concat(validFiles),updatePreview()});function updatePreview(){preview.innerHTML="",selectedFiles.forEach((file,index)=>{const fileReader=new FileReader;fileReader.onload=function(e){const fileURL=e.target.result,container=document.createElement("div");container.style.position="relative",container.style.display="flex",container.style.alignItems="center";let element;file.type.startsWith("image/")?(element=document.createElement("img"),element.src=fileURL,element.alt=file.name):file.type.startsWith("video/")&&(element=document.createElement("video"),element.src=fileURL,element.controls=!1),element&&(element.style.width="60px",element.style.height="60px",element.style.borderRadius="4px",element.style.objectFit="cover",container.appendChild(element));const deleteButton=document.createElement("button");deleteButton.style.position="absolute",deleteButton.style.top="0",deleteButton.style.right="0",deleteButton.style.width="18px",deleteButton.style.height="18px",deleteButton.style.border="none",deleteButton.style.background=`url(${preview_close_btn}) no-repeat center/cover`,deleteButton.style.cursor="pointer",deleteButton.addEventListener("click",function(){removeFile(index)}),container.appendChild(deleteButton),preview.appendChild(container)},fileReader.readAsDataURL(file)})}function removeFile(index){selectedFiles.splice(index,1),updateFileInput(),updatePreview()}function updateFileInput(){const dataTransfer=new DataTransfer;selectedFiles.forEach(file=>dataTransfer.items.add(file)),fileInput.files=dataTransfer.files}function showErrorModal(message){let miniModalContent=`
                    <div style="display: flex; gap: 12px; flex-direction: column; align-items: center;">
                        <div class="body-1" style="color:#000;">\uD30C\uC77C \uC5C5\uB85C\uB4DC \uC2E4\uD328</div>
                        <div class="body-2 text-tertiary">${message}</div>
                    </div>
                    <div class="close_btn body-3" style="cursor:pointer; padding: 6px 24px;margin-top: 40px;border-radius: 4px;border: 1px solid #D6DADE;">\uB2EB\uAE30</div>
                `;openMiniModalWithContent(miniModalContent,()=>{document.querySelector(".close_btn").addEventListener("click",()=>{document.getElementById("site-mini-modal").classList.remove("active")})})}function handleInput(inputElement,countElement,maxCount){inputElement.addEventListener("input",function(){const currentCharCount=inputElement.value.length;countElement.textContent=currentCharCount.toLocaleString(),currentCharCount>maxCount&&(alert(`\uCD5C\uB300 ${maxCount}\uC790\uC758 \uC785\uB825\uB9CC \uAC00\uB2A5\uD569\uB2C8\uB2E4.`),inputElement.value=inputElement.value.substring(0,maxCount),countElement.textContent=maxCount.toLocaleString())})}const maxTitleCount=40,maxDescCount=2e3,titleInput=document.querySelector(".inquiry_title"),titleCount=document.querySelector(".title-text_count"),descInput=document.querySelector(".inquiry_desc"),descCount=document.querySelector(".desc-text_count");handleInput(titleInput,titleCount,maxTitleCount),handleInput(descInput,descCount,maxDescCount);function askFormData(){const formData=new FormData,askFormTitle=document.querySelector(".inquiry_title").value,askFormDesc=document.querySelector(".inquiry_desc").value,inquiryType=document.querySelector(".inquiry_type").value;function getFormattedDate(){const now=new Date,adjusted=new Date(now.getTime()-540*60*1e3),year=adjusted.getFullYear(),month=String(adjusted.getMonth()+1).padStart(2,"0"),day=String(adjusted.getDate()).padStart(2,"0"),hours=String(adjusted.getHours()).padStart(2,"0"),minutes=String(adjusted.getMinutes()).padStart(2,"0"),seconds=String(adjusted.getSeconds()).padStart(2,"0");return`${year}-${month}-${day}T${hours}:${minutes}:${seconds}`}const created_at=getFormattedDate(),requestData={customerMd5Hash,customer_name:`${customer_name}`,type:inquiryType,submitted_at:created_at,status:"\uBBF8\uD655\uC778",title:askFormTitle,content:askFormDesc};return formData.append("data",JSON.stringify(requestData)),selectedFiles.forEach(file=>{const fileExtension=file.name.slice((file.name.lastIndexOf(".")-1>>>0)+2),now=new Date,year=now.getFullYear(),month=String(now.getMonth()+1).padStart(2,"0"),day=String(now.getDate()).padStart(2,"0"),timestamp=`${year}${month}${day}`,characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";let randomString="";for(let i=0;i<8;i++)randomString+=characters.charAt(Math.floor(Math.random()*characters.length));const newFileName=`inquire_${timestamp}_${randomString}.${fileExtension}`,newFile=new File([file],newFileName,{type:file.type,lastModified:file.lastModified});formData.append("fileList",newFile)}),formData}function handleFormValidationAndSubmit(){const askFormTitle=document.querySelector(".inquiry_title"),askFormDesc=document.querySelector(".inquiry_desc"),inquiryType=document.querySelector(".inquiry_type"),applyBtn=document.querySelector(".apply-ask_btn");if(!applyBtn)return;const checkFormValidity=()=>askFormTitle.value.trim()!==""&&askFormDesc.value.trim()!==""&&inquiryType.value!==""&&inquiryType.selectedIndex!==0?(applyBtn.classList.add("active"),!0):(applyBtn.classList.remove("active"),!1);askFormTitle.addEventListener("input",checkFormValidity),askFormDesc.addEventListener("input",checkFormValidity),inquiryType.addEventListener("change",checkFormValidity),checkFormValidity(),applyBtn.addEventListener("click",()=>{if(openLoadingModal(),checkFormValidity(),!applyBtn.classList.contains("active")){closeLoadingModal();return}let resultData=askFormData(),jsonObject={};resultData.forEach((value,key)=>{jsonObject[key]=value}),fetch("https://sidiz-shopify.sidiz.com/inquire/create",{method:"POST",body:resultData}).then(response=>{if(!response.ok)throw new Error(`HTTP error! status: ${response.status}`);return response.json()}).then(data=>{data.status==="success"&&data.success===!0?(closeAlertModal(),setTimeout(()=>{closeLoadingModal(),openMiniModalWithContent(`
                                    <div style="display: flex; flex-direction: column; gap: 40px; align-items: center;">
                                        <div style="display: flex; flex-direction: column; gap: 12px; align-items: center;">
                                            <div class="body-1" style="color:#000;">1:1 \uBB38\uC758\uAC00 \uC811\uC218\uB418\uC5C8\uC2B5\uB2C8\uB2E4.</div>
                                            <div class="body-2" style="color:#7C8084;">\uB2F4\uB2F9\uC790 \uD655\uC778 \uD6C4 \uBE60\uB978 \uC2DC\uC77C \uB0B4\uC5D0 \uC548\uB0B4 \uB4DC\uB9AC\uACA0\uC2B5\uB2C8\uB2E4.</div>
                                        </div>
                                        <div style="display: flex; flex-direction: row; gap: 8px; align-items: center;">
                                            <div style="cursor:pointer; width:126px; padding:6px; 24px; border:1px solid #D6DADE; border-radius:4px; color:#000; text-align:center;" class="body-3 onotoone_modal">\uB2EB\uAE30</div>
                                            <div style="cursor:pointer; width:126px; padding:6px; 24px; border:1px solid #7C8084; border-radius:4px; color:#000; text-align:center;" class="body-3 showMyAsk">\uBB38\uC758 \uB0B4\uC5ED \uBCF4\uAE30</div>
                                        </div>
                                    </div>
                                `,()=>{document.querySelector(".onotoone_modal").addEventListener("click",()=>{closeMiniModal(),location.reload()}),document.querySelector(".showMyAsk").addEventListener("click",()=>{closeMiniModal(),setCookie("redirect",JSON.stringify({type:"tab",to:"ask"}),1),window.location.href="/account"})})},3e3)):(closeAlertModal(),closeLoadingModal(),openMiniModalWithContent(`
                                <div style="display: flex; flex-direction: column; gap: 40px; align-items: center;">
                                    <div style="display: flex; flex-direction: column; gap: 12px; align-items: center;">
                                        <div class="body-1" style="color:#000;">\uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0 \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.</div>
                                    </div>
                                    <div style="display: flex; flex-direction: row; gap: 8px; align-items: center;">
                                        <div style="cursor:pointer; width:126px; padding:6px; 24px; border:1px solid #D6DADE; border-radius:4px; color:#000; text-align:center;" class="body-3 onotoone_modal">\uB2EB\uAE30</div>
                                    </div>
                                </div>
                            `,()=>{document.querySelector(".onotoone_modal").addEventListener("click",()=>{closeMiniModal(),location.reload()})}))}).catch(error=>{closeAlertModal(),closeLoadingModal(),openMiniModalWithContent(`
                            <div style="display: flex; flex-direction: column; gap: 40px; align-items: center;">
                                <div style="display: flex; flex-direction: column; gap: 12px; align-items: center;">
                                    <div class="body-1" style="color:#000;">\uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0 \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.</div>
                                </div>
                                <div style="display: flex; flex-direction: row; gap: 8px; align-items: center;">
                                    <div style="cursor:pointer; width:126px; padding:6px; 24px; border:1px solid #D6DADE; border-radius:4px; color:#000; text-align:center;" class="body-3 onotoone_modal">\uB2EB\uAE30</div>
                                </div>
                            </div>
                        `,()=>{document.querySelector(".onotoone_modal").addEventListener("click",()=>{closeMiniModal(),location.reload()})})})})}handleFormValidationAndSubmit()}):commonLoginModal("oneToOneModal")}function setCookie(cookieName,value,exdays){const exdate=new Date;exdate.setDate(exdate.getDate()+exdays);let cookieValue=encodeURIComponent(value)+"; path=/;";exdays&&(cookieValue+=" expires="+exdate.toUTCString()+";"),document.cookie=cookieName+"="+cookieValue}
//# sourceMappingURL=/cdn/shop/t/152/assets/customers-onetoone-inquiry.js.map
