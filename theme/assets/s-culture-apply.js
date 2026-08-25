const HTMLGenerators={generateLabel:(name,description="")=>`
        <p class="form_field_name">${name}<span style="color : #FF3A4A">*</span></p>
        <div class="form_field_input">
            ${description?`<div class="form_field_description body-3 text-secondary">${description}</div>`:""}
    `,generateSingleLineText:field=>`
            ${HTMLGenerators.generateLabel(field.name,field.description)}
            <input type="text" data-field_key="${field.key}" name="${field.key}" placeholder=""/>
        </div>
    `,generateDropdown:field=>`
        ${HTMLGenerators.generateLabel(field.name,field.description)}
        <select data-field_key="${field.key}" name="${field.key}">
            <option value="" disabled selected hidden>\uC635\uC158\uC744 \uC120\uD0DD\uD574 \uC8FC\uC138\uC694.</option>
            ${field.choices.map(choice=>`<option value="${choice}">${choice}</option>`).join("")}
        </select>
    </div>
    `,generateLinearScale:field=>{const{min,max}=field.validations||{};return typeof min!="number"||typeof max!="number"?"":`
            ${HTMLGenerators.generateLabel(field.name,field.description)}
            <div class="linear-scale-wrapper">
                <div class="linear-scale">
                    ${Array.from({length:max-min+1},(_,i)=>{const num=min+i;return`
                            <div class="scale-item">
                                <input type="radio" 
                                    id="${field.key}_${num}"
                                    name="${field.key}" 
                                    value="${num}" 
                                    data-field_key="${field.key}"
                                />
                                <label for="${field.key}_${num}">
                                    <span class="scale-line"></span>
                                    <span class="scale-num">${num}</span>
                                </label>
                            </div>
                        `}).join("")}
                </div>
            </div>
        `},generateSingleCheckbox:field=>`
            ${HTMLGenerators.generateLabel(field.name,field.description)}
            <div class="checkbox-group" onclick="handleSingleCheckbox(event)">
                ${field.choices.map(choice=>`
                    <label class="checkbox-item">
                        <input type="checkbox" 
                            name="${field.key}" 
                            value="${choice}" 
                            data-field_key="${field.key}"
                        />
                        <div class="text-secondary body-3">${choice}</div>
                    </label>
                `).join("")}
            </div>
        </div>
    `,generateMultipleCheckbox:field=>`
            ${HTMLGenerators.generateLabel(field.name,field.description)}
            <div class="checkbox-group">
                ${field.choices.map(choice=>`
                    <label class="checkbox-item">
                        <input type="checkbox" 
                            name="${field.key}" 
                            value="${choice}" 
                            data-field_key="${field.key}"
                        />
                        <div class="text-secondary body-3">${choice}</div>
                    </label>
                `).join("")}
            </div>
        </div>
    `,generateImageUpload:field=>`
            ${HTMLGenerators.generateLabel(field.name,field.description)}
            <div class="s_culture_img_wrapper">
                <input type="file"
                    name="${field.key}" 
                    accept="image/png, image/jpeg, image/jpg, image/gif, image/bmp, image/webp"
                    multiple 
                    data-field_key="${field.key}"
                    id="${field.key}"
                    class="hidden"
                />
                <label for="${field.key}" class="s_culture_add_img">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
                        <path d="M8 3V13" stroke="black" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"></path>
                        <path d="M3 8H13" stroke="black" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"></path>
                    </svg>
                </div>
                <!-- preview\uC601\uC5ED -->
            </div>
        </div>
    `};function generateFieldHTML(field){let html="";switch(field.key.includes("-")?field.key.split("-")[0]:field.key){case"text":html=HTMLGenerators.generateSingleLineText(field);break;case"select":html=HTMLGenerators.generateDropdown(field);break;case"linear":html=HTMLGenerators.generateLinearScale(field);break;case"check":html=HTMLGenerators.generateSingleCheckbox(field);break;case"checks":html=HTMLGenerators.generateMultipleCheckbox(field);break;case"image_file":html=HTMLGenerators.generateImageUpload(field);break;default:console.warn(`\uC54C \uC218 \uC5C6\uB294 field.key: ${field.key}`);break}return html}async function fetchCultureFormData(sectionId,type,modalTitle,modalAdditional,matchedApplyMapping){try{const response=await fetch("https://sidiz-shopify.sidiz.com/s-culture/apply/form",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({type})});if(!response.ok)throw new Error("\uC11C\uBC84 \uC751\uB2F5 \uC624\uB958");const result=await response.json();result.success&&result.result?sCultureApplyBtn(sectionId,result,modalTitle,modalAdditional):console.error("\uC815\uC0C1\uC801\uC778 \uB370\uC774\uD130\uB97C \uBC1B\uC9C0 \uBABB\uD588\uC2B5\uB2C8\uB2E4.",result)}catch(error){console.error("API \uD638\uCD9C \uC2E4\uD328:",error)}}function sCultureApplyBtn(sectionId,data,modalTitle,modalAdditional){if(!data||!Array.isArray(data.result)||data.result.length===0){console.error("\uC62C\uBC14\uB978 \uB370\uC774\uD130 \uD615\uC2DD\uC774 \uC544\uB2D9\uB2C8\uB2E4.");return}const descHTML=modalAdditional.additional_desc?`<div class="additional-desc desc"><p>${modalAdditional.additional_desc}</p></div>`:"",imagesHTML=modalAdditional.additional_images?.length>0?`<div class="additional-images" style="margin-top: 8px;">
                ${modalAdditional.additional_images.map(url=>`
                    <img src="${url}" style="max-width: 100%; height: auto; display: block; margin-bottom: 8px;" />
                `).join("")}
            </div>`:"";let topContent="",bottomContent="";modalAdditional.additional_t_position==="top"?topContent+=descHTML:modalAdditional.additional_t_position==="bottom"&&(bottomContent+=descHTML),modalAdditional.additional_p_position==="top"?topContent+=imagesHTML:modalAdditional.additional_p_position==="bottom"&&(bottomContent+=imagesHTML),topContent&&(topContent=`<div class="additional-section" style="padding-bottom: 28px;">${topContent}</div>`),bottomContent&&(bottomContent=`<div class="additional-section" style="padding-top: 28px;">${bottomContent}</div>`);const agreementContent=`
        <div style="margin-top: 16px;">
            <div class="select-all">
                <input type="checkbox" name="sculture-all-agree" id="sculture-all-agree">
                <label for="sculture-all-agree">\uC804\uCCB4 \uB3D9\uC758</label>
            </div>

            <div class="s-culture-contour"></div>

            <div class="individual-selection">
                <div class="individual-selection--text">
                    <input type="checkbox" name="sculture-agree-1" id="sculture-agree-1">
                    <label for="sculture-agree-1" style="display: flex; flex-direction: row; align-items: center;">
                        <span class="blue" style="margin:0 1px 0 2px;">(\uD544\uC218)&nbsp;</span>\uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758
                    </label>
                </div>
                <p id="sculture-btn-1" class="first_policy">\uBCF4\uAE30</p>
            </div>
            <div class="individual-selection" style="margin-top: 4px;">
                <div class="individual-selection--text">
                    <input type="checkbox" name="sculture-agree-2" id="sculture-agree-2">
                    <label for="sculture-agree-2" style="display: flex; flex-direction: row; align-items: center;">
                        <span class="blue" style="margin:0 1px 0 2px;">(\uD544\uC218)&nbsp;</span>\uAC1C\uC778\uC815\uBCF4 \uC81C 3\uC790 \uC81C\uACF5 \uB3D9\uC758
                    </label>
                </div>
                <p id="sculture-btn-2" class="second_policy">\uBCF4\uAE30</p>
            </div>
        </div>
    `,formFields=data.result.map(field=>`
        <div class="form-field" data-field-type="${field.key}">
            ${generateFieldHTML(field)}
        </div>
    `).join(""),modalContent=`
        <div id="formModal" class="s-culture-form" data-section-id="${sectionId}">
            <div class="form_wrapper">
                ${topContent}
                ${formFields}
                ${bottomContent}
                ${agreementContent}
            </div>
        </div>

        <!-- \uAC1C\uC778\uC815\uBCF4 \uC815\uCC45 \uC601\uC5ED -->
        <div class="sculture-policy-1" style="display: none;">
            <div class="terms-modal-container">
                <div class="terms-modal-title">[\uD544\uC218] \uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758</div>
                <table>
                    <thead>
                        <tr>
                            <th colspan="2">\uD56D\uBAA9</th>
                            <th>\uBAA9\uC801</th>
                            <th>\uBCF4\uC720 \uBC0F \uC774\uC6A9 \uAE30\uAC04</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>\uD544\uC218</td>
                            <td>\uC774\uB984, \uD578\uB4DC\uD3F0 \uBC88\uD638, \uC8FC\uC18C, SNS\uACC4\uC815, \uCD08\uC0C1\uAD8C(\uC0AC\uC9C4)</td>
                            <td>\uBCF8\uC778 \uC2DD\uBCC4, \uACBD\uD488 \uBC1C\uC1A1, \uC815\uBCF4 \uACF5\uC9C0, \uB9CC\uC871\uB3C4 \uC870\uC0AC</td>
                            <td>\uD68C\uC6D0\uD0C8\uD1F4 \uB610\uB294 \uC0AD\uC81C \uC694\uCCAD \uC2DC</td>
                        </tr>
                    </tbody>
                </table>
                <div class="terms-modal-text">
                    &#8251; \uB3D9\uC758 \uAC70\uBD80 \uC2DC \uC11C\uBE44\uC2A4 \uC774\uC6A9\uC774 \uC81C\uD55C\uB420 \uC218 \uC788\uC2B5\uB2C8\uB2E4.
                </div>
            </div>
        </div>

        <div class="sculture-policy-2" style="display: none;">
            <div class="terms-modal-container">
                <div class="terms-modal-title">[\uD544\uC218] \uAC1C\uC778\uC815\uBCF4 \uC81C 3\uC790 \uC81C\uACF5 \uB3D9\uC758</div>
                <table>
                    <thead>
                        <tr>
                            <th colspan="2">\uD56D\uBAA9</th>
                            <th>\uC815\uBCF4\uB97C \uC81C\uACF5\uBC1B\uB294 \uC790</th>
                            <th>\uBAA9\uC801</th>
                            <th>\uBCF4\uC720 \uBC0F \uC774\uC6A9 \uAE30\uAC04</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>\uD544\uC218</td>
                            <td>\uC774\uB984, \uD578\uB4DC\uD3F0 \uBC88\uD638, \uC8FC\uC18C, SNS\uACC4\uC815, \uCD08\uC0C1\uAD8C(\uC0AC\uC9C4)</td>
                            <td>\uD3F4\uC564\uB9C8\uD06C,\uD06C\uB9AC\uC5D0\uC774\uD301</td>
                            <td>\uBCF8\uC778 \uC2DD\uBCC4 \uBC0F \uACBD\uD488 \uBC1C\uC1A1 \uB4F1</td>
                            <td>\uC804\uC790\uC0C1\uAC70\uB798\uBC95\uC5D0 \uB530\uB77C 5\uB144 \uBCF4\uAD00</td>
                        </tr>
                    </tbody>
                </table>
                <div class="terms-modal-text">
                    &#8251; \uB3D9\uC758 \uAC70\uBD80 \uC2DC \uC11C\uBE44\uC2A4 \uC774\uC6A9\uC774 \uC81C\uD55C\uB420 \uC218 \uC788\uC2B5\uB2C8\uB2E4.
                </div>
            </div>
        </div>

        <div class="s_culture_apply_btn_wrapper">
            <button type="button" class="s_culture_apply_btn" onclick="applyForm('${modalTitle}')">\uC2E0\uCCAD\uD558\uAE30</button>
        </div>
    `;openModalWithContent(modalTitle+" \uC2E0\uCCAD"||"S-CULTURE \uC2E0\uCCAD",modalContent,()=>{document.querySelector(".modal--contents").style.marginBottom="104px",showPolicySculture(modalTitle),checkAllBoxSculture(),document.querySelectorAll('input[type="file"]').forEach(fileInput=>{fileInput&&initFileUpload(fileInput.id)}),document.getElementById("formModal").querySelectorAll("[data-field_key]").forEach(el=>{el.addEventListener("input",checkFormCompletion),el.addEventListener("change",checkFormCompletion)}),checkFormCompletion(),document.querySelectorAll("select[data-field_key]").forEach(select=>{select.style.color=select.value===""?"#b4b9be":"#000",select.addEventListener("change",function(){this.style.color=this.value===""?"#b4b9be":"#000"})})})}function checkFormCompletion(){const formElement=document.getElementById("formModal"),submitButton=document.querySelector(".s_culture_apply_btn");let checkAllInput=document.getElementById("sculture-all-agree"),isComplete=!0;checkAllInput.checked||(isComplete=!1),formElement.querySelectorAll("[data-field_key]").forEach(el=>{const value=el.value.trim();el.type==="file"?el.files.length===0&&(isComplete=!1):el.type==="checkbox"?formElement.querySelector(`[name="${el.name}"]:checked`)||(isComplete=!1):el.type==="radio"?formElement.querySelector(`[name="${el.name}"]:checked`)||(isComplete=!1):value===""&&(isComplete=!1)}),isComplete?(submitButton.disabled=!1,submitButton.classList.add("active")):(submitButton.disabled=!0,submitButton.classList.remove("active"))}function applyForm(modalTitle){const sectionId=document.getElementById("formModal").dataset.sectionId,type=(document.getElementById(sectionId)?.querySelector(".s-culture-apply .wrapper > div")).dataset.type,matchedApplyMapping=window.sCultureApplyMappings.find(mapping=>mapping.s_culture_apply_key===type);if(!matchedApplyMapping){openMiniModalWithContent(`
            <div class="s-culture-result">
                <div class="result_wrapper">
                    <div class="body-1">
                        \uC2E0\uCCAD \uC815\uBCF4\uB97C \uCC3E\uC744 \uC218 \uC5C6\uC2B5\uB2C8\uB2E4.
                    </div>
                </div>
                <div class="close_btn body-3">\uB2EB\uAE30</div>
            </div>
        `,()=>{document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),location.reload(!0)})});return}const now=new Date,start=new Date(matchedApplyMapping.apply_start_dt),end=new Date(matchedApplyMapping.apply_end_dt);if(now<start){openMiniModalWithContent(`
            <div class="s-culture-result">
                <div class="result_wrapper">
                    <div class="body-1">
                        \uC2E0\uCCAD\uC774 \uC544\uC9C1 \uC2DC\uC791\uB418\uC9C0 \uC54A\uC558\uC2B5\uB2C8\uB2E4.
                    </div>
                </div>
                <div class="close_btn body-3">\uB2EB\uAE30</div>
            </div>
        `,()=>{document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),location.reload(!0)})});return}if(now>end){openMiniModalWithContent(`
            <div class="s-culture-result">
                <div class="result_wrapper">
                    <div class="body-1">
                        \uC2E0\uCCAD\uC774 \uB9C8\uAC10\uB418\uC5C8\uC2B5\uB2C8\uB2E4.
                    </div>
                </div>
                <div class="close_btn body-3">\uB2EB\uAE30</div>
            </div>
        `,()=>{document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),location.reload(!0)})});return}openLoadingModal();const sCultureData=new FormData,formElement=document.getElementById("formModal");function getFormattedDate(){const now2=new Date,adjusted=new Date(now2.getTime()-540*60*1e3),year=adjusted.getFullYear(),month=String(adjusted.getMonth()+1).padStart(2,"0"),day=String(adjusted.getDate()).padStart(2,"0"),hours=String(adjusted.getHours()).padStart(2,"0"),minutes=String(adjusted.getMinutes()).padStart(2,"0"),seconds=String(adjusted.getSeconds()).padStart(2,"0");return`${year}-${month}-${day}T${hours}:${minutes}:${seconds}`}let createdTime=getFormattedDate();sCultureData.append("type",type);const requestData={customerMd5Hash,customer_name,created_at:createdTime},checkboxMultipleMap={};formElement.querySelectorAll("[data-field_key]").forEach(el=>{const key=el.name,value=el.value?.trim?.()||"",isMultipleCheckbox=el.dataset.field_key==="checks";if(el.type==="file"){el.files&&el.files.length>0&&Array.from(el.files).forEach(file=>{sCultureData.append("fileList",file)});return}if(el.type==="checkbox"){el.checked&&(isMultipleCheckbox?(checkboxMultipleMap[key]||(checkboxMultipleMap[key]=[]),checkboxMultipleMap[key].push(el.value)):requestData[key]=el.value);return}if(el.type==="radio"){el.checked&&(requestData[key]=el.value);return}value!==""&&(requestData[key]=value)}),Object.entries(checkboxMultipleMap).forEach(([key,values])=>{requestData[key]=values}),sCultureData.append("data",JSON.stringify(requestData)),fetch("https://sidiz-shopify.sidiz.com/s-culture/apply",{method:"POST",body:sCultureData,mode:"cors",credentials:"include"}).then(async response=>{const resData=await response.json();if(!response.ok||resData.success===!1)throw new Error(resData.msg||"\uC2E0\uCCAD \uCC98\uB9AC \uC911 \uC624\uB958 \uBC1C\uC0DD");closeAlertModal(),sCulturResultModal(resData,modalTitle)}).catch(error=>{closeAlertModal(),console.error("\uC5D0\uB7EC:",error),sCulturResultModal({success:!1,msg:error.message||"\uC54C \uC218 \uC5C6\uB294 \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4.",modalTitle})}).finally(()=>{closeLoadingModal()})}function initFileUpload(inputId){const fileInput=document.getElementById(inputId);if(!fileInput){console.error(`ID\uAC00 '${inputId}'\uC778 file input\uC744 \uCC3E\uC744 \uC218 \uC5C6\uC2B5\uB2C8\uB2E4.`);return}const preview=document.createElement("div");preview.classList.add("preview-container"),fileInput.parentElement.appendChild(preview);let selectedFiles=[];const MAX_FILES=5,IMAGE_MAX_SIZE=5*1024*1024,allowedExtensions=["png","jpg","jpeg","gif","bmp","webp"];fileInput.addEventListener("change",function(event){handleFileSelection(event)});function handleFileSelection(event){const files=Array.from(event.target.files),processedFiles=[];for(const file of files){const renamed=validateAndRenameFile(file);renamed!==!1&&processedFiles.push(renamed)}if(selectedFiles.length+processedFiles.length>MAX_FILES){showErrorModal(`\uCD5C\uB300 ${MAX_FILES}\uAC1C\uC758 \uD30C\uC77C\uB9CC \uC5C5\uB85C\uB4DC\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4.`),fileInput.value="";return}selectedFiles=selectedFiles.concat(processedFiles),updateFileInput(),updatePreview()}function validateAndRenameFile(file){const fileExtension=file.name.split(".").pop().toLowerCase();return allowedExtensions.includes(fileExtension)?file.size>IMAGE_MAX_SIZE?(showErrorModal("\uC774\uBBF8\uC9C0\uB294 \uCD5C\uB300 5MB\uAE4C\uC9C0 \uC5C5\uB85C\uB4DC\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4."),fileInput.value="",!1):renameFile(file):(showErrorModal("\uC9C0\uC6D0\uD558\uC9C0 \uC54A\uB294 \uD30C\uC77C \uD615\uC2DD\uC785\uB2C8\uB2E4."),fileInput.value="",!1)}function updatePreview(){preview.innerHTML="",selectedFiles.forEach((file,index)=>{const fileReader=new FileReader;fileReader.onload=function(e){const container=document.createElement("div");container.classList.add("preview-item"),container.style.position="relative";let element;file.type.startsWith("image/")&&(element=document.createElement("img"),element.src=e.target.result),element&&(element.classList.add("preview-image"),element.style.width="60px",element.style.height="60px",element.style.objectFit="cover",element.style.borderRadius="4px",element.style.pointerEvents="none",container.appendChild(element));const deleteButton=document.createElement("button");deleteButton.style.position="absolute",deleteButton.style.top="0",deleteButton.style.right="0",deleteButton.style.width="18px",deleteButton.style.height="18px",deleteButton.style.border="none",deleteButton.style.background=`url(${preview_close_btn}) no-repeat center/cover`,deleteButton.style.cursor="pointer",deleteButton.addEventListener("click",function(){removeFile(index)}),container.appendChild(deleteButton),preview.appendChild(container)},fileReader.readAsDataURL(file)})}function removeFile(index){selectedFiles.splice(index,1),updateFileInput(),updatePreview(),checkFormCompletion()}function updateFileInput(){const dataTransfer=new DataTransfer;selectedFiles.forEach(file=>dataTransfer.items.add(file)),fileInput.files=dataTransfer.files}return function(){return selectedFiles}}function handleSingleCheckbox(event){event.target.type==="checkbox"&&event.target.closest(".checkbox-group").querySelectorAll('input[type="checkbox"]').forEach(checkbox=>{checkbox!==event.target&&(checkbox.checked=!1)})}function sCulturResultModal(data,modalTitle){const isSuccess=data?.success===!0;let modalContent=`
        <div class="s-culture-result">
            <div class="result_wrapper">
                <div class="body-1">
                    ${isSuccess?`${modalTitle||"S-Culture"} \uC2E0\uCCAD\uC774 \uC644\uB8CC\uB418\uC5C8\uC2B5\uB2C8\uB2E4.`:`${modalTitle||"S-Culture"} \uC2E0\uCCAD\uC5D0 \uC2E4\uD328\uD558\uC600\uC2B5\uB2C8\uB2E4.`}
                </div>
                <div class="body-2 text-tertiary">
                    ${isSuccess?"\uB9C8\uC774\uD398\uC774\uC9C0\uC5D0\uC11C \uC2E0\uCCAD \uB0B4\uC5ED\uC744 \uD655\uC778\uD558\uC138\uC694.":"\uB2E4\uC2DC \uD55C\uBC88 \uC2E0\uCCAD\uD574\uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4."}
                </div>
            </div>
            <div class="confirm_btn_wrapper" style="display: flex;gap: 8px;">
                ${isSuccess?`
                <div class="confirm_btn body-3" style="border: 1px solid #7C8084;    
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 96px;
                    border-radius: 4px;
                cursor: pointer;">\uB9C8\uC774\uD398\uC774\uC9C0</div>`:""}
                <div class="close_btn body-3">\uB2EB\uAE30</div>
            </div>
        </div>
    `;isSuccess==!0&&window.dataLayer.push({event:"register_sculture",page_type:window.pageType,click_text:document.querySelector(".modal--title p").innerText||"_"}),openMiniModalWithContent(modalContent,()=>{document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),location.reload(!0)}),document.querySelector(".confirm_btn")?.addEventListener("click",()=>{closeMiniModal(),location.href="/account?tab=sCulture"})})}function showErrorModal(message){let miniModalContent=`
        <div style="display: flex; gap: 12px; flex-direction: column; align-items: center;">
            <div class="body-1" style="color:#000;">\uD30C\uC77C \uC5C5\uB85C\uB4DC \uC2E4\uD328</div>
            <div class="body-2 text-tertiary">${message}</div>
        </div>
        <div class="close_btn body-3" style="padding: 6px 24px; margin-top:40px;">\uB2EB\uAE30</div>
    `;openMiniModalWithContent(miniModalContent,()=>{document.querySelector(".close_btn").addEventListener("click",()=>{document.getElementById("site-mini-modal").classList.remove("active")})})}function renameFile(file){const fileExtension=file.name.slice((file.name.lastIndexOf(".")-1>>>0)+2),now=new Date,year=now.getFullYear(),month=String(now.getMonth()+1).padStart(2,"0"),day=String(now.getDate()).padStart(2,"0"),timestamp=`${year}${month}${day}`,characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";let randomString="";for(let i=0;i<8;i++)randomString+=characters.charAt(Math.floor(Math.random()*characters.length));const newFileName=`s-culture-apply_${timestamp}_${randomString}.${fileExtension}`;return new File([file],newFileName,{type:file.type,lastModified:file.lastModified})}function showPolicySculture(modalTitle){const modalWrapper=document.querySelector(".s-culture-form"),modalHeader=document.querySelector(".modal--header"),modalButton=document.querySelector(".s_culture_apply_btn_wrapper"),createBackButtonSculture=()=>{const backButton=document.createElement("button");return backButton.innerHTML=`
        <span style="display:flex; padding: 4px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M9.1875 2.1875L4.375 7L9.1875 11.8125" stroke="white" stroke-width="1.2" stroke-linecap="square" style="mix-blend-mode:exclusion"/>
            </svg>
        </span>`,backButton.className="back-button",modalHeader.prepend(backButton),backButton},titleElement=modalHeader.querySelector("p");[1,2].forEach(num=>{const button=document.querySelector(`#sculture-btn-${num}`),policy=document.querySelector(`.sculture-policy-${num}`);button.addEventListener("click",()=>{modalWrapper.style.display="none",modalButton.style.display="none",document.querySelectorAll('[class^="sculture-policy-"]').forEach(content=>{content.style.display="none"}),policy.style.display="block";const backButton=createBackButtonSculture();num===1?titleElement.textContent="\uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758":num===2&&(titleElement.textContent="\uAC1C\uC778\uC815\uBCF4 \uC81C 3\uC790 \uC81C\uACF5 \uB3D9\uC758"),backButton.addEventListener("click",()=>{modalWrapper.style.display="block",document.querySelectorAll('[class^="sculture-policy-"]').forEach(content=>{content.style.display="none"}),backButton.remove(),modalButton.style.display="flex",titleElement.textContent=`${modalTitle} \uC2E0\uCCAD`}),document.querySelector(".modal--close_btn").addEventListener("click",()=>{backButton.remove()})})})}function checkAllBoxSculture(){const checkAll=document.getElementById("sculture-all-agree"),checkIndividualList=document.querySelectorAll("#sculture-agree-1, #sculture-agree-2");checkAll.addEventListener("click",()=>{checkIndividualList.forEach(checkIndividual=>{checkIndividual.checked=checkAll.checked}),checkFormCompletion()}),checkIndividualList.forEach(checkIndividual=>{checkIndividual.addEventListener("change",()=>{const isAllChecked=Array.from(checkIndividualList).every(check=>check.checked);checkAll.checked=isAllChecked,checkFormCompletion()})})}
//# sourceMappingURL=/cdn/shop/t/152/assets/s-culture-apply.js.map
