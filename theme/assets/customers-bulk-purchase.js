let content,startText="\uC0AC\uC5C5\uC790 \uAD6C\uB9E4 \uBB38\uC758\uB97C \uC6D0\uD558\uC2DC\uB294 \uACBD\uC6B0 \uC694\uCCAD \uC815\uBCF4\uB97C \uC791\uC131\uD574 \uC8FC\uC138\uC694.<br>\uB2F4\uB2F9\uC790 \uD655\uC778 \uD6C4 \uC21C\uCC28\uC801\uC73C\uB85C \uC548\uB0B4\uB4DC\uB9AC\uACA0\uC2B5\uB2C8\uB2E4.";const purLoc=`
    <p>\uC0AC\uC5C5\uC790\uBA85(\uD68C\uC0AC\uBA85)<span class="red">*</span></p>
    <input type="text" value="" class="user-purchase-location" placeholder="\uC0AC\uC5C5\uC790\uBA85(\uD68C\uC0AC\uBA85)\uC744 \uC785\uB825\uD574 \uC8FC\uC138\uC694.">
    <p class="user-purchase-location-msg"></p>
`,address=`
    <div class="addr_title"><p>\uB0A9\uD488 \uC8FC\uC18C\uC9C0</p> <button type="button" class="find_addr">\uC8FC\uC18C\uCC3E\uAE30</button></div>
    <input type="text" value="" name="user_addr1" readonly class="user_addr1" placeholder="\uC6B0\uD3B8\uBC88\uD638">
    <input type="text" value="" name="user_addr2" readonly class="user_addr2" placeholder="\uB3C4\uB85C\uBA85 \uC8FC\uC18C">
    <input type="text" value="" name="user_addr3" class="user_addr3" placeholder="\uC0C1\uC138\uC8FC\uC18C">
`,purItem=`
    <p>\uC81C\uD488\uBA85(\uC81C\uD488\uCF54\uB4DC)</p>
    <input type="text" value="" placeholder="\uAD6C\uB9E4\uD558\uC2E4 \uC81C\uD488\uBA85 \uD639\uC740 \uC81C\uD488\uCF54\uB4DC\uB97C \uC785\uB825\uD574 \uC8FC\uC138\uC694.">
`,purItemCount=`
    <p>\uC608\uC0C1 \uAD6C\uB9E4 \uC218\uB7C9</p>
    <input type="number" value="" placeholder="\uAD6C\uB9E4 \uC218\uB7C9\uC744 \uC785\uB825\uD574\uC8FC\uC138\uC694.">
`,userPhNum=`
    <p>\uD734\uB300\uD3F0 \uBC88\uD638<span class="red">*</span></p>
    <input type="text" value="" class="user-phone-num" placeholder="\uC22B\uC790\uB9CC \uC785\uB825\uC774 \uAC00\uB2A5\uD569\uB2C8\uB2E4.('-'\uC81C\uC678)">
    <p class="user-phone-num-msg hiddenMsg"></p>
`,userEmail=`
    <p>\uC774\uBA54\uC77C<span class="red">*</span></p>
    <input type="text" value="" class="user-email" placeholder="\uC774\uBA54\uC77C\uC744 \uC785\uB825\uD574 \uC8FC\uC138\uC694.">
    <p class="user-email-msg hiddenMsg"></p>
`,userRequestMaxText=1e3,userRequest=`
    <div class="user-request-title">
        <p>\uC694\uCCAD\uC0AC\uD56D</p> <p><span class="char-count">0</span>/<span>1,000</span></p>
    </div>
    <textarea class="user-request-area" name="" id="" cols="30" rows="10" placeholder="\uC6B4\uC601\uC815\uCC45\uACFC \uB9DE\uC9C0 \uC54A\uB294 \uBE44\uBC29\uC131 \uAE00 / \uC695\uC124 \uB4F1\uC740 \uC0AD\uC81C\uB429\uB2C8\uB2E4. \uAC1C\uC778\uC815\uBCF4, \uACB0\uC81C\uC815\uBCF4\uB294 \uAE30\uC7AC \uBD88\uAC00\uD558\uBA70 \uC791\uC131 \uC2DC \uC784\uC758 \uC0AD\uC81C \uB420 \uC218 \uC788\uC2B5\uB2C8\uB2E4."></textarea>
`,policyCheckBox=`
    <div class="select-all">
        <input type="checkbox" name="policy-all-agree" id="policy-all-agree">
        <label for="policy-all-agree">
            <p class="body-4" style="color: var(--text-secondary, #434548);">\uC804\uCCB4 \uB3D9\uC758</p>
        </label>
    </div>

    <div class="contour"></div>

    <div class="individual-selection hidden">
        <div class="individual-selection--text">
            <input type="checkbox" name="policy-one-agree" id="policy-one-agree">
            <label for="policy-one-agree">
                <p class="body-4" style="color: var(--text-secondary, #434548);"><span class="blue" style="margin-right:1px;">(\uD544\uC218) </span>\uC1FC\uD551\uBAB0 \uC774\uC6A9 \uC57D\uAD00</p>
            </label>
        </div>
        <p class="first_policy">\uBCF4\uAE30</p>
    </div>
    <div class="individual-selection">
        <div class="individual-selection--text">
            <input type="checkbox" name="policy-two-agree" id="policy-two-agree">
            <label for="policy-two-agree">
                <p class="body-4" style="color: var(--text-secondary, #434548);"><span class="blue" style="margin-right:1px;">(\uD544\uC218) </span>\uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758</p>
            </label>
        </div>
        <p class="second_policy">\uBCF4\uAE30</p>
    </div>
`,applyBtn=`
    <button type="button" class="apply_btn_bulk">\uC811\uC218\uD558\uAE30</button>
`,bulk_links=document.querySelectorAll(".bulk_link .wrapper > div");bulk_links.forEach(link=>{link.addEventListener("click",function(e){e.preventDefault(),content=`
            <div class="bulk">
                <div class="bulk-wrapper">
                    <div class="desc"><p>${startText}</p></div> <!-- desc -->
                    <div class="bulk-input-wrapper">
                        <div class="purchase-location">${purLoc}</div> <!-- \uC0AC\uC5C5\uC790\uBA85(\uD68C\uC0AC\uBA85) * -->
                        <div class="delivery-address">${address}</div> <!-- \uB0A9\uD488 \uC8FC\uC18C\uC9C0 -->
                        <div class="purchase-item-name">${purItem}</div> <!-- \uC81C\uD488\uBA85 -->
                        <div class="purchase-item-count">${purItemCount}</div> <!-- \uC608\uC0C1 \uAD6C\uB9E4\uC218\uB7C9 -->
                        <div class="user-phone-num-wrapper">${userPhNum}</div> <!-- \uD578\uB4DC\uD3F0\uBC88\uD638 * -->
                        <div class="user-email-wrapper">${userEmail}</div> <!-- \uC774\uBA54\uC77C * -->
                        <div class="user-request">${userRequest}</div> <!-- \uC694\uCCAD\uC0AC\uD56D -->
                    </div>
                    <div class="policy-check-box">${policyCheckBox}</div> <!-- \uB3D9\uC758 \uD56D\uBAA9 -->
                </div>
                <div class="button-wrapper">${applyBtn}</div> <!-- \uC2E0\uCCAD \uBC84\uD2BC -->
            </div>
    
            <div class="policy-1">${shopTermsService}</div>
            <div class="policy-2">
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
                                <td>\uAD6C\uB9E4\uCC98, \uD734\uB300\uD3F0 \uBC88\uD638, \uC774\uBA54\uC77C</td>
                                <td rowspan="2">
                                    \uC0AC\uC5C5\uC790 \uAD6C\uB9E4 \uBB38\uC758 \uC751\uB300
                                </td>
                                <td rowspan="2">
                                    \uBAA9\uC801 \uB2EC\uC131 60\uC77C \uD6C4 \uC9C0\uCCB4\uC5C6\uC774 \uD30C\uAE30
                                </td>
                            </tr>
                            <tr>
                                <td>\uC120\uD0DD</td>
                                <td>\uB0A9\uD488 \uC8FC\uC18C\uC9C0</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="terms-modal-text">
                        &#8251; \uC815\uBCF4\uC8FC\uCCB4\uB294 \uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9\uC5D0 \uB3D9\uC758\uD558\uC9C0 \uC54A\uC744 \uAD8C\uB9AC\uAC00 \uC788\uC73C\uBA70, \uB3D9\uC758\uB97C \uAC70\uBD80\uD560 \uACBD\uC6B0 \uC11C\uBE44\uC2A4 \uC774\uC6A9\uC774 \uC81C\uD55C\uB429\uB2C8\uB2E4.
                    </div>
                </div>
            </div>
        `,openModalWithContent("\uC0AC\uC5C5\uC790 \uAD6C\uB9E4 \uBB38\uC758",content,function(){let modalContents=document.querySelector(".modal--contents");modalContents.style.height="auto";const inputPhoneNumber=document.querySelector(".user-phone-num");inputPhoneNumber.addEventListener("input",()=>{let value=inputPhoneNumber.value.replace(/[^0-9]/g,"");value=value.slice(0,11),value.length>7?value=value.slice(0,3)+"-"+value.slice(3,7)+"-"+value.slice(7):value.length>3&&(value=value.slice(0,3)+"-"+value.slice(3)),inputPhoneNumber.value=value}),countUserRequestTextBulk(".user-request-area",".char-count"),document.querySelector(".find_addr").addEventListener("click",findMyAddrBulk),setupCheckboxesBulk(),checkPurchaseFormBulk(),document.querySelector(".apply_btn_bulk").addEventListener("click",function(){submitBulkForm()});const policy1=document.querySelector(".first_policy"),policy2=document.querySelector(".second_policy");policy1.addEventListener("click",function(){showPolicyBulk(".policy-1","\uC1FC\uD551\uBAB0 \uC774\uC6A9 \uC57D\uAD00")}),policy2.addEventListener("click",function(){showPolicyBulk(".policy-2","\uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758")})}),window.dataLayer.push({event:"click_business_inquiry",page_type:"\uBE44\uC988\uB2C8\uC2A4",click_text:"\uC2E0\uCCAD\uD558\uAE30"})})});function countUserRequestTextBulk(textareaSelector,counterSelector){const textarea=document.querySelector(textareaSelector),counter=document.querySelector(counterSelector);textarea.addEventListener("input",function(){let charCount=textarea.value.length;charCount>1e3&&(textarea.value=textarea.value.substring(0,1e3),charCount=1e3),counter.textContent=charCount})}function findMyAddrBulk(){new daum.Postcode({oncomplete:function(data){const postalCode=data.zonecode,roadAddr=data.roadAddress;document.querySelector(".user_addr1").value=postalCode,document.querySelector(".user_addr2").value=roadAddr}}).open()}function setupCheckboxesBulk(){const allAgreeCheckbox=document.querySelector("#policy-all-agree"),individualCheckboxes=document.querySelectorAll("input#policy-two-agree");allAgreeCheckbox.addEventListener("change",function(){individualCheckboxes.forEach(function(checkbox){checkbox.checked=allAgreeCheckbox.checked}),updateCheckBoxStatusBulk()}),individualCheckboxes.forEach(function(checkbox){checkbox.addEventListener("change",function(){const allChecked=Array.from(individualCheckboxes).every(function(individualCheckbox){return individualCheckbox.checked});allAgreeCheckbox.checked=allChecked,updateCheckBoxStatusBulk()})})}let checkForm,chkCheckBox;function checkPurchaseFormBulk(){const inputPurchaseLocation=document.querySelector(".user-purchase-location"),inputPhoneNumber=document.querySelector(".user-phone-num"),inputEmail=document.querySelector(".user-email"),purchaseLocationMsgElement=document.querySelector(".user-purchase-location-msg"),phoneNumberMsgElement=document.querySelector(".user-phone-num-msg"),emailMsgElement=document.querySelector(".user-email-msg"),phonePattern=/^(01[016789]{1})[0-9]{4}[0-9]{4}$/,emailPattern=/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;let isPurchaseLocationValid=!1,isPhoneNumberValid=!1,isEmailValid=!1;function validatePurchaseLocationBulk(){inputPurchaseLocation.value===""?(purchaseLocationMsgElement.textContent="\uAD6C\uB9E4\uCC98\uB97C \uC785\uB825\uD574 \uC8FC\uC138\uC694.",purchaseLocationMsgElement.classList.remove("hiddenMsg"),isPurchaseLocationValid=!1):(purchaseLocationMsgElement.textContent="",purchaseLocationMsgElement.classList.add("hiddenMsg"),isPurchaseLocationValid=!0),updateCheckFormStatusBulk()}function validatePhoneNumberBulk(){let phoneNumber=inputPhoneNumber.value;phoneNumber=phoneNumber.replace(/[^0-9]/g,"");const phonePattern2=/^[0-9]{10,11}$/;inputPhoneNumber.value===""?(phoneNumberMsgElement.textContent="\uD734\uB300\uD3F0 \uBC88\uD638\uB97C \uC785\uB825\uD574 \uC8FC\uC138\uC694.",phoneNumberMsgElement.classList.remove("hiddenMsg"),isPhoneNumberValid=!1):phonePattern2.test(phoneNumber)?(phoneNumberMsgElement.textContent="",phoneNumberMsgElement.classList.add("hiddenMsg"),isPhoneNumberValid=!0):(phoneNumberMsgElement.textContent="\uC815\uD655\uD55C \uBC88\uD638\uB97C \uC785\uB825\uD574 \uC8FC\uC138\uC694.",phoneNumberMsgElement.classList.remove("hiddenMsg"),isPhoneNumberValid=!1),updateCheckFormStatusBulk()}function validateEmailBulk(){const email=inputEmail.value.trim();email===""?(emailMsgElement.textContent="\uC774\uBA54\uC77C\uC744 \uC785\uB825\uD574 \uC8FC\uC138\uC694.",emailMsgElement.classList.remove("hiddenMsg"),isEmailValid=!1):emailPattern.test(email)?(emailMsgElement.textContent="",inputEmail.style.border="none",emailMsgElement.classList.add("hiddenMsg"),isEmailValid=!0):(emailMsgElement.textContent="*\uC62C\uBC14\uB978 \uC774\uBA54\uC77C \uD615\uC2DD\uC73C\uB85C \uC785\uB825\uD574\uC8FC\uC138\uC694.",emailMsgElement.classList.remove("hiddenMsg"),isEmailValid=!1),updateCheckFormStatusBulk()}function updateCheckFormStatusBulk(){checkForm=isPurchaseLocationValid&&isPhoneNumberValid&&isEmailValid,updateApplyButtonStatusBulk()}inputPurchaseLocation.addEventListener("input",validatePurchaseLocationBulk),inputPhoneNumber.addEventListener("input",validatePhoneNumberBulk),inputEmail.addEventListener("input",validateEmailBulk),updateCheckFormStatusBulk()}function updateCheckBoxStatusBulk(){const allAgreeCheckbox=document.querySelector("#policy-all-agree"),oneAgreeCheckbox=document.querySelector("#policy-one-agree"),twoAgreeCheckbox=document.querySelector("#policy-two-agree");allAgreeCheckbox.checked=twoAgreeCheckbox.checked,chkCheckBox=allAgreeCheckbox.checked,updateApplyButtonStatusBulk()}function updateApplyButtonStatusBulk(){const applyButton=document.querySelector(".apply_btn_bulk");checkForm&&chkCheckBox?applyButton.classList.add("active"):applyButton.classList.remove("active")}function bulkFrom(){const formData=new FormData,purchaseLocation=document.querySelector(".user-purchase-location").value.trim(),postalCode=document.querySelector(".user_addr1").value.trim(),roadAddress=document.querySelector(".user_addr2").value.trim(),detailAddress=document.querySelector(".user_addr3").value.trim(),productName=document.querySelector(".purchase-item-name input").value.trim(),productCount=document.querySelector(".purchase-item-count input").value.trim(),phoneNumber=document.querySelector(".user-phone-num").value.trim().replace(/-/g,""),email=document.querySelector(".user-email").value.trim(),userRequestData=document.querySelector(".user-request-area").value.trim();function getFormattedDate(){const now=new Date,adjusted=new Date(now.getTime()-540*60*1e3),year=adjusted.getFullYear(),month=String(adjusted.getMonth()+1).padStart(2,"0"),day=String(adjusted.getDate()).padStart(2,"0"),hours=String(adjusted.getHours()).padStart(2,"0"),minutes=String(adjusted.getMinutes()).padStart(2,"0"),seconds=String(adjusted.getSeconds()).padStart(2,"0");return`${year}-${month}-${day}T${hours}:${minutes}:${seconds}`}let createdTime=getFormattedDate();formData.append("buyer_name",purchaseLocation),formData.append("zip_code",postalCode||""),formData.append("address",roadAddress||""),formData.append("address_detail",detailAddress||""),formData.append("product_info",productName||""),formData.append("qty",productCount||""),formData.append("phone_number",phoneNumber),formData.append("email",email),formData.append("request",userRequestData.replace(/\n/g,"\\n").replace(/\r/g,"\\r")),formData.append("created_at",createdTime);const policyOneAgree=document.querySelector("#policy-one-agree").checked?"true":"false",policyTwoAgree=document.querySelector("#policy-two-agree").checked?"true":"false";return formData.append("policyOneAgree",policyOneAgree),formData.append("policyTwoAgree",policyTwoAgree),formData}function submitBulkForm(){const formData=bulkFrom();let jsonObject={};formData.forEach((value,key)=>{jsonObject[key]=value}),fetch("https://sidiz-shopify.sidiz.com/bulk/create",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({data:jsonObject})}).then(response=>{if(!response.ok)throw new Error(`HTTP error! status: ${response.status}`);return closeAlertModal(),response.json()}).then(data=>{openMiniModalWithContent(`
            <div class="success-bulk-modal">
                <p>\uBB38\uC758 \uC2E0\uCCAD\uC774 \uC644\uB8CC\uB418\uC5C8\uC2B5\uB2C8\uB2E4.</p>
                <p>\uB2F4\uB2F9\uC790 \uD655\uC778 \uD6C4 \uC21C\uCC28\uC801\uC73C\uB85C \uC5F0\uB77D\uB4DC\uB9B4 \uC608\uC815\uC785\uB2C8\uB2E4.</p>
                <button class="body-4 bulk-success-btn">\uD655\uC778</button>
            </div>
        `,function(){document.querySelector(".bulk-success-btn").addEventListener("click",function(){closeMiniModal()})}),window.dataLayer.push({event:"submit_business_inquiry",page_type:"\uBE44\uC988\uB2C8\uC2A4",business_info:jsonObject.buyer_name||"_",ce_item_name:jsonObject.product_info||"_",expected_quantity:Number(jsonObject.qty)})}).catch(error=>{openMiniModalWithContent(`
            <div class="success-bulk-modal">
                <p>
                    \uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.<br>
                    \uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0 \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.
                </p>
                <button class="body-4 bulk-success-btn">\uD655\uC778</button>
            </div>
        `,function(){document.querySelector(".bulk-success-btn").addEventListener("click",function(){closeMiniModal()})})})}function showPolicyBulk(policyClass,titleText){document.querySelector(".modal--contents_warpper").scrollTop=0,document.querySelector(".bulk").style.display="none",document.querySelector(`${policyClass}`).style.display="block";const arrow=`<svg xmlns="http://www.w3.org/2000/svg" width="14" height="15" viewBox="0 0 14 15" fill="none">
							<path d="M9.1875 2.6875L4.375 7.5L9.1875 12.3125" stroke="white" stroke-width="1.2" stroke-linecap="square" style="mix-blend-mode:exclusion"></path>
						</svg>`,backBtn=document.createElement("div");backBtn.innerHTML=arrow,backBtn.classList.add("backButton"),document.querySelector(".modal--header").prepend(backBtn),document.querySelector(".modal--title p").textContent=titleText,backBtn.addEventListener("click",function(){document.querySelector(`${policyClass}`).style.display="none",document.querySelector(".bulk").style.display="block",backBtn.remove(),document.querySelector(".modal--title p").textContent="\uC0AC\uC5C5\uC790 \uAD6C\uB9E4 \uBB38\uC758"}),document.querySelector(".modal--close_btn").addEventListener("click",function(){backBtn.remove(),document.querySelector(".modal--title p").textContent="\uC0AC\uC5C5\uC790 \uAD6C\uB9E4 \uBB38\uC758"})}
//# sourceMappingURL=/cdn/shop/t/152/assets/customers-bulk-purchase.js.map
