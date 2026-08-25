function commonLoginModal(urlParamText,clickType="default"){const login_btn=[{id:"kakao",name:"\uCE74\uCE74\uC624",svg:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                    <path d="M10 1.66797C4.48276 1.66797 0 4.83464 0 8.83464C0 10.8346 1.2069 12.668 3.10345 14.0013V18.3346L7.24138 15.668C8.10345 15.8346 8.96552 16.0013 10 16.0013C15.5172 16.0013 20 12.8346 20 8.83464C20 4.83464 15.5172 1.66797 10 1.66797Z" fill="black"/>
                </svg>`},{id:"naver",name:"\uB124\uC774\uBC84",svg:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                    <path d="M19 2V18H12.9599L7.04012 9.94656V18H1V2H7.04012L12.9599 10.3804V2H19Z" fill="#06BE34"/>
                </svg>`},{id:"email",name:"\uC774\uBA54\uC77C",svg:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                    <path d="M16 1.42969L4.00001 4.58306V9.00239C3.99955 9.04832 4.01415 9.0931 4.04151 9.12966C4.06887 9.16623 4.10743 9.19249 4.15111 9.20431L13.0744 11.55L4.00001 13.9416V18.5725L16 15.4192V11.0059C16.0005 10.96 15.9859 10.9152 15.9585 10.8786C15.9311 10.842 15.8926 10.8158 15.8489 10.804L6.90066 8.45224L16 6.0606V1.42969Z" fill="white" style="mix-blend-mode:exclusion"/>
                </svg>`}],savedIdFlag=getCookie("save-id-flag")==="true";let savedIdValue="";function getCookie(name){const parts=`; ${document.cookie}`.split(`; ${name}=`);if(parts.length===2)return parts.pop().split(";").shift()}const cookieIdValue=decodeURIComponent(getCookie("save-id-value"));cookieIdValue!=="undefined"&&cookieIdValue!=null&&(savedIdValue=cookieIdValue);let modalTitle="LOG IN",clickTypeText="\uBC30\uB108";clickType==="wishlist"&&(clickTypeText="\uBC30\uB108_to_wishlist");let modalContent=`
        <div class="text-secondary body-2 pls_login">\uB85C\uADF8\uC778\uC774 \uD544\uC694\uD55C \uC11C\uBE44\uC2A4\uC785\uB2C8\uB2E4.</div>
        <div class="select-login" style="">
            <div style="display:flex; flex-direction:column; gap:20px; width:100%">
                <div class="login-btn_wrapper" style="">
                ${login_btn.map((button,index)=>{let background,border;return index===0?(background="#FAE100",border="none"):(background="#FFF",border="1px solid var(--border-basic2, #D6DADE)"),`
                        <button id="${button.id}" type="button" class='login-btn gtm-login' data-gtm-click-type="\uBC30\uB108" data-gtm-click-text="${button.name} \uB85C\uADF8\uC778" style='background:${background}; border:${border};'>
                            <div class="login-btb--svg" style="display:flex; padding:4px;">
                                ${button.svg}
                            </div>
                            <div>
                                <p class="modal-login-btn-text">${button.name} \uB85C\uADF8\uC778</p>
                            </div>
                        </button>
                        `}).join("")}
                </div>
                <div class="findId_Pw" style="">
                    <!-- <button class="member__conversion" style="width:fit-content; padding:4px 2px;"><p class="body-3" style="color: var(--text-tertiary, #7C8084);margin:0;">\uAE30\uC874 \uD68C\uC6D0 \uC804\uD658</p></button>
                    <div style="display:flex; padding:4px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                            <rect x="6.39844" width="1.2" height="14" fill="#D6DADE"/>
                        </svg>
                    </div> -->
                    <button class="find__id"><p class="body-3">\uC544\uC774\uB514 \uCC3E\uAE30</p></button>
                    <div style="display:flex; padding:4px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                            <rect x="6.39844" width="1.2" height="14" fill="#D6DADE"/>
                        </svg>
                    </div>
                    <button class="find__pw"><p class="body-3">\uBE44\uBC00\uBC88\uD638 \uCC3E\uAE30</p></button>
                </div>
            </div>

            <div class="login_modal-footer">
                <p class="body-3 login_modal-footer-text">\uC2DC\uB514\uC988 \uD68C\uC6D0\uC5D0\uAC8C \uC8FC\uC5B4\uC9C0\uB294 \uCFE0\uD3F0\uACFC \uCD94\uCC9C\uC778 \uD61C\uD0DD\uC744 \uB204\uB9AC\uC138\uC694.</p>
                <p class="login_modal-footer-join gtm-sign-up" data-gtm-click-type="${clickTypeText}" data-gtm-click-text="\uD68C\uC6D0\uAC00\uC785">\uD68C\uC6D0\uAC00\uC785</p>
            </div>
        </div>

        <div class="login_modal-form_wrapper" style="">
            <form action="/account/login" method="post" style="height:100%;">
                <div class="login_modal_form_flex">
                    <div>
                        <div class="login_modal_id-pw_wrapper">
                            <div class="login_modal_form__id_wrapper">
                                <label for="login-modal_customer_email" class="body-2">\uC544\uC774\uB514(\uC774\uBA54\uC77C)</label>
                                <input
                                    class="param_user input_user_email body-2"
                                    type="email"
                                    value="${savedIdValue}"
                                    name="customer[email]"
                                    id="login-modal_customer_email"
                                    data-param_type="user_email"
                                    data-check_result="F"
                                    placeholder="\uC544\uC774\uB514(\uC774\uBA54\uC77C)\uC744 \uC785\uB825\uD574 \uC8FC\uC138\uC694."
                                    autocorrect="off"
                                    autocapitalize="off"
                                    autofocus
                                >
                                <div class="err__msg hidden msg_user_email "style="color:#ff0000; font-size:14px;font-weight:300; letter-spacing:-0.025em;"></div>
                            </div>

                            <div class="login_modal_form__pw_wrapper">
                                <label class="body-2" style=";" for="login-modal_customer_password">\uBE44\uBC00\uBC88\uD638</label>
                                <div class="input-container input_user_password" style="">
                                    <input
                                        class="param_user body-2"
                                        type="password"
                                        value=""
                                        name="customer[password]"
                                        id="login-modal_customer_password"
                                        data-param_type="user_pw"
                                        data-check_result="F"
                                        placeholder="\uBE44\uBC00\uBC88\uD638\uB97C \uC785\uB825\uD574\uC8FC\uC138\uC694"
                                        style="padding:13px 12px; flex-grow: 1; outline: none; border:none; border-radius: 4px; height:50px;"
                                    >
                                    <button type="button" id='toggle_password' style="background-image: url(${login_modal_pw_unshow});"></button>
                                </div>
                            <div class="err__msg hidden msg_user_pw" style="color:#ff0000; font-size:14px;font-weight:300; letter-spacing:-0.025em;"></div>
                        </div>

                        <div class="login-modal_id-value-wrapper">
                            <div class="login-modal_saveId" >
                                <input type="checkbox" id="scales" name="remember_user" ${savedIdFlag?"checked":""}>
                                <label class="body-4" " for="scales">\uC544\uC774\uB514 \uC800\uC7A5</label>
                            </div>

                            <div class="login-modal_find-id-pw-wrapper">
                                <div class="login-modal_find-id" data-link_type="user_email" >
                                    <a href="/pages/customers-find-user_email" style="">\uC544\uC774\uB514 \uCC3E\uAE30</a>
                                </div>
                                <div style="padding:4px; display: flex; align-items: center;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                                        <rect x="6.39844" width="1.2" height="14" fill="#D6DADE"/>
                                    </svg>
                                </div>
                                <div class="login-modal_find-pw" data-link_type="user_pw">
                                    <a href="/pages/customers-find-user_pw">\uBE44\uBC00\uBC88\uD638 \uCC3E\uAE30</a>
                                </div>
                            </div>
                        </div>  
                    </div>
                            
                    <div class="form-actions flex-buttons">
                        <button class="login_btn">\uB85C\uADF8\uC778 \uD558\uAE30</button>
                    </div>
                </div>

                <div class="login_modal_div__user__regist">
                    <div class="body-3 login_modal_div__user__regist-text">\uC2DC\uB514\uC988 \uD68C\uC6D0\uC5D0\uAC8C \uC8FC\uC5B4\uC9C0\uB294 \uCFE0\uD3F0\uACFC \uCD94\uCC9C\uC778 \uD61C\uD0DD\uC744 \uB204\uB9AC\uC138\uC694.</div>
                    <div class="btn__join text-select gtm-sign-up" data-link_type="user_regist" data-gtm-click-type="${clickTypeText}" data-gtm-click-text="\uD68C\uC6D0\uAC00\uC785">\uD68C\uC6D0\uAC00\uC785</div>
                </div>
                </div>
            </form>
        </div>
    `;openModalWithContent(modalTitle,modalContent,()=>{document.querySelector(".modal--contents").style.height="425px",document.querySelector(".modal--contents_warpper").style.height="auto",document.querySelector(".modal--contents_warpper").style.paddingBottom="40px";const joinLink=document.querySelector(".login_modal-footer-join"),joinLink2=document.querySelector(".btn__join"),memberConversion=document.querySelector(".member__conversion"),findId=document.querySelector(".find__id"),findPw=document.querySelector(".find__pw"),kakaoLoginBtn=document.getElementById("kakao"),naverLoginBtn=document.getElementById("naver"),emailLoginBtn=document.getElementById("email");let nowLocation=location.href.split(".com")[1];[{element:joinLink,action:()=>{sessionStorage.setItem("prev_url",nowLocation),location.href="/account/register"}},{element:joinLink2,action:()=>location.href="/account/register"},{element:memberConversion,action:()=>location.href="/pages/customers-convert-user"},{element:findId,action:()=>location.href="/pages/customers-find-user_email"},{element:findPw,action:()=>location.href="/pages/customers-find-user_pw"}].forEach(button=>{button.element&&button.element.addEventListener("click",button.action)}),emailLoginBtn&&emailLoginBtn.addEventListener("click",function(e){e.preventDefault();const plsLoginTxt=document.querySelector(".pls_login"),emailLoginForm=document.querySelector(".login_modal-form_wrapper"),selectLogin=document.querySelector(".select-login"),modalHeader=document.querySelector(".modal--header"),closeModalBtn=modalHeader.querySelector(".modal--close_btn"),modalTitle2=document.querySelector(".modal--header .modal--title p");plsLoginTxt.style.display="none",modalTitle2.innerText="\uC774\uBA54\uC77C\uB85C \uB85C\uADF8\uC778",emailLoginForm.style.display="block",selectLogin.style.display="none";let backButton=modalHeader.querySelector(".back-button");backButton||(backButton=document.createElement("button"),backButton.innerHTML=`
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="15" viewBox="0 0 14 15" fill="none">
                            <path d="M9.1875 2.6875L4.375 7.5L9.1875 12.3125" stroke="white" stroke-width="1.2" stroke-linecap="square" style="mix-blend-mode:exclusion"/>
                        </svg>
                    `,backButton.className="back-button",backButton.style.border="none",backButton.style.background="none",backButton.style.display="flex",backButton.style.padding="4px",backButton.style.cursor="pointer",backButton.addEventListener("click",function(){plsLoginTxt.style.display="block",emailLoginForm.style.display="none",selectLogin.style.display="flex",modalTitle2.innerText="LOG IN",backButton.remove()}),modalHeader.prepend(backButton),closeModalBtn.addEventListener("click",()=>{backButton.remove()})),showPw();const uId=document.getElementById("login-modal_customer_email"),uPw=document.getElementById("login-modal_customer_password");checkIdPw(uId,uPw),document.querySelector(".login_btn").addEventListener("click",e2=>{e2.preventDefault(),openLoadingModal(),checkUser(uId.value).then(emailExists=>{if(emailExists){const formData=new URLSearchParams;formData.append("customer[email]",uId.value),formData.append("customer[password]",uPw.value),fetch("/account/login",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:formData.toString(),credentials:"include"}).then(response=>{if(closeLoadingModal(),response.redirected&&response.url.includes("/account/login")){let msg_pw=document.querySelector(".msg_user_pw");msg_pw.textContent="\uBE44\uBC00\uBC88\uD638\uAC00 \uC77C\uCE58\uD558\uC9C0 \uC54A\uC2B5\uB2C8\uB2E4.",msg_pw.classList.remove("hidden")}else{if(urlParamText&&urlParamText.trim()!==""){const newUrl=new URL(window.location.href);newUrl.searchParams.set(urlParamText,"true"),window.history.pushState({},"",newUrl)}document.querySelector("#scales").checked?(document.cookie="save-id-flag=true; path=/",document.cookie=`save-id-value=${encodeURIComponent(uId.value)}; path=/`):(document.cookie="save-id-flag=false; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC;",document.cookie="save-id-value=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC;"),localStorage.setItem("gtmCustomerEvent","L"),localStorage.setItem("gtmCustomerLoginMethod","Email"),kakaoPixel("6421355729020341302").pageView(),kakaoPixel("6421355729020341302").login();try{const body=JSON.stringify({customer_id:uId.value}),blob=new Blob([body],{type:"application/json"});navigator.sendBeacon("https://sidiz-shopify.sidiz.com/v1/coupons/login-auto-issue",blob)}catch(e3){console.warn("\u26A0\uFE0F \uCFE0\uD3F0 \uBC1C\uAE09 \uC694\uCCAD \uC2E4\uD328 (beacon \uC804\uC1A1 \uC624\uB958):",e3)}location.reload()}})}else closeLoadingModal()})})}),kakaoLoginBtn&&kakaoLoginBtn.addEventListener("click",function(){let oauth_kakao="https://kauth.kakao.com/oauth/",client_kakao="fc74e41fba98520112740ae101843b2c",redirect_kakao="https://kr.sidiz.com/pages/kakao-login";sessionStorage.setItem("action_type","LOGIN"),sessionStorage.setItem("prev_url",nowLocation);let tmp_url=`${oauth_kakao}authorize?client_id=${client_kakao}&redirect_uri=${redirect_kakao}&response_type=code`;location.href=tmp_url,sessionStorage.setItem(urlParamText,"true")}),naverLoginBtn&&naverLoginBtn.addEventListener("click",function(){let oauth_naver="https://nid.naver.com/oauth2.0/",client_naver="VY9Euld75KN5q1u0upZD",redirect_naver=encodeURI("https://kr.sidiz.com/pages/naver-login"),mt=Date.now().toString(),rand=Math.random().toString(),state=CryptoJS.MD5(mt+rand).toString();sessionStorage.setItem("action_type","LOGIN"),sessionStorage.setItem("prev_url",nowLocation);let tmp_url=`${oauth_naver}authorize?response_type=code&client_id=${client_naver}&redirect_uri=${redirect_naver}&state=${state}`;location.href=tmp_url,sessionStorage.setItem(urlParamText,"true")})}),document.querySelectorAll(".gtm-login").forEach(btn=>{btn.addEventListener("click",()=>{let clickUrl="";switch(btn.dataset.gtmClickText){case"\uCE74\uCE74\uC624 \uB85C\uADF8\uC778":clickUrl="https://kr.sidiz.com/pages/kakao-login";break;case"\uB124\uC774\uBC84 \uB85C\uADF8\uC778":clickUrl="https://kr.sidiz.com/pages/naver-login";break;default:clickUrl="https://kr.sidiz.com/account/login";break}window.dataLayer.push({event:"click_login",page_type:window.pageType,click_type:btn.dataset.gtmClickType,click_text:btn.dataset.gtmClickText,click_url:clickUrl})})}),document.querySelectorAll(".gtm-sign-up").forEach(btn=>{btn.addEventListener("click",()=>{window.dataLayer.push({event:"click_sign_up",page_type:window.pageType,click_type:btn.dataset.gtmClickType,click_text:btn.dataset.gtmClickText,click_url:"https://kr.sidiz.com/account/register"})})});function showPw(){const passwordInput=document.getElementById("login-modal_customer_password"),toggleButton=document.getElementById("toggle_password");toggleButton.addEventListener("click",function(){passwordInput.type==="password"?(passwordInput.type="text",toggleButton.style.backgroundImage=`url(${login_modal_pw_show})`):(passwordInput.type="password",toggleButton.style.backgroundImage=`url(${login_modal_pw_unshow})`)})}function checkUser(param_email){const emailErrorMsg=document.querySelector(".msg_user_email");return fetch("https://sidiz-shopify.sidiz.com/v1/email-check",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:param_email})}).then(response=>{if(!response.ok)throw new Error(`HTTP error! status: ${response.status}`);return response.json()}).then(data=>data.code==="0001"?!0:(data.code==="0002"&&(emailErrorMsg.textContent="\uC785\uB825\uD55C \uD68C\uC6D0\uC815\uBCF4\uAC00 \uC5C6\uC2B5\uB2C8\uB2E4.",emailErrorMsg.classList.remove("hidden")),!1)).catch(error=>!1)}function checkIdPw(id,pw){const emailMsgElement=document.querySelector(".msg_user_email"),passwordMsgElement=document.querySelector(".msg_user_pw"),emailPattern=/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,passwordPattern=/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^*+=-?]).{8,16}$/;function validateEmail(){const email=id.value.trim();email===""?(emailMsgElement.textContent="\uC544\uC774\uB514(\uC774\uBA54\uC77C) \uBBF8\uC785\uB825",emailMsgElement.classList.remove("hidden")):emailPattern.test(email)?(emailMsgElement.textContent="",emailMsgElement.classList.add("hidden")):(emailMsgElement.textContent="\uC62C\uBC14\uB978 \uC774\uBA54\uC77C \uD615\uC2DD\uC774 \uC544\uB2D9\uB2C8\uB2E4. ",emailMsgElement.classList.remove("hidden"))}function validatePassword(){const password=pw.value;password===""?(passwordMsgElement.textContent="\uBE44\uBC00\uBC88\uD638 \uBBF8\uC785\uB825",passwordMsgElement.classList.remove("hidden")):passwordPattern.test(password)?(passwordMsgElement.textContent="",passwordMsgElement.classList.add("hidden")):(passwordMsgElement.textContent="*\uD2B9\uC218\uBB38\uC790, \uC601\uBB38 \uB300\uC18C\uBB38\uC790, \uC22B\uC790 \uD3EC\uD568 8\uC790 \uC774\uC0C1",passwordMsgElement.classList.remove("hidden"))}id.addEventListener("input",validateEmail),pw.addEventListener("input",validatePassword)}}
//# sourceMappingURL=/cdn/shop/t/152/assets/login-modal.js.map
