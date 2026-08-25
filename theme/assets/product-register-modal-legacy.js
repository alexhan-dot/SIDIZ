(function(){const API_ENDPOINT="https://sidiz-shopify.sidiz.com/v1/db/serial-registration",DEFAULT_TITLE="\uC0C8\uB85C\uC6B4 \uC815\uD488 \uB4F1\uB85D\uD558\uAE30",REGEX_SERIAL=/^[a-zA-Z0-9-]*$/,REGEX_SERIAL_DASHES=/[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]/g,REGEX_ZERO_WIDTH=/[\u200B-\u200D\uFEFF]/g,ERROR_MESSAGES={normal:{500:"\uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574\uC8FC\uC138\uC694.<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",501:"\uC798\uBABB\uB41C \uC2DC\uB9AC\uC5BC \uB118\uBC84\uC785\uB2C8\uB2E4.<br>\uD655\uC778 \uD6C4 \uB2E4\uC2DC \uC785\uB825\uD574 \uC8FC\uC138\uC694<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",502:"\uD488\uC9C8\uBCF4\uC99D\uAE30\uD55C\uC774 \uB4F1\uB85D\uB418\uC9C0 \uC54A\uC740 \uC81C\uD488\uC785\uB2C8\uB2E4.<br> \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",503:"\uB124\uD2B8\uC6CC\uD06C \uC5F0\uACB0\uC774 \uC6D0\uD65C\uD558\uC9C0 \uC54A\uC2B5\uB2C8\uB2E4.<br><br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",default:"\uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574\uC8FC\uC138\uC694.<br>\uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4."},system:{500:"\uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574\uC8FC\uC138\uC694.<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",501:"\uC798\uBABB\uB41C \uC2DC\uB9AC\uC5BC \uB118\uBC84\uC785\uB2C8\uB2E4.<br>\uD655\uC778 \uD6C4 \uB2E4\uC2DC \uC785\uB825\uD574 \uC8FC\uC138\uC694<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",502:"\uD488\uC9C8\uBCF4\uC99D\uAE30\uD55C\uC774 \uB4F1\uB85D\uB418\uC9C0 \uC54A\uC740 \uC81C\uD488\uC785\uB2C8\uB2E4.<br> \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",503:"\uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574\uC8FC\uC138\uC694.<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.",default:"\uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.<br>\uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0 \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758\uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4."}},DEFAULT_OPTIONS={title:DEFAULT_TITLE,apiEndpoint:API_ENDPOINT,successMode:"detail",successMessage:"\uC815\uD488 \uB4F1\uB85D\uC774 \uC644\uB8CC\uB418\uC5C8\uC2B5\uB2C8\uB2E4.<br/>\uC2DC\uB514\uC988\uAC00 \uC81C\uACF5\uD558\uB294 \uD488\uC9C8 \uBCF4\uC99D \uC11C\uBE44\uC2A4\uB97C \uACBD\uD5D8\uD574 \uBCF4\uC138\uC694.",detailSuccessText:"\uC81C\uD488\uC774 \uB4F1\uB85D\uB418\uC5C8\uC2B5\uB2C8\uB2E4.",detailPrimaryCtaText:"\uC790\uC138\uD788 \uBCF4\uAE30",detailPrimaryCtaUrl:"/account?tab=my_product",detailSecondaryCtaText:"\uB2EB\uAE30",shareContainerSelector:".wrapper__my_product",errorTone:"normal"};let activeState=null;function getGlobalString(name){return typeof window[name]=="string"||typeof window[name]<"u"?window[name]:""}function getLexicalGlobal(name){switch(name){case"img_product_ex":return typeof img_product_ex<"u"?img_product_ex:"";case"shopTermsService":return typeof shopTermsService<"u"?shopTermsService:"";case"icon_share_line_bk":return typeof icon_share_line_bk<"u"?icon_share_line_bk:"";case"icon_close_line_bk":return typeof icon_close_line_bk<"u"?icon_close_line_bk:"";case"icon_close_line_wh":return typeof icon_close_line_wh<"u"?icon_close_line_wh:"";case"icon_sns_kakao":return typeof icon_sns_kakao<"u"?icon_sns_kakao:"";case"icon_sns_link":return typeof icon_sns_link<"u"?icon_sns_link:"";case"customerMd5Hash":return typeof customerMd5Hash<"u"?customerMd5Hash:"";case"pageType":return typeof pageType<"u"?pageType:"";case"allProductData":return typeof allProductData<"u"?allProductData:void 0;default:return""}}function getIcon(name){const lexicalValue=getLexicalGlobal(name);return lexicalValue||getGlobalString(name)||""}function resolveOptions(options){const merged={...DEFAULT_OPTIONS,...options||{}};return ERROR_MESSAGES[merged.errorTone]||(merged.errorTone="normal"),merged}function getImgProductEx(){return getLexicalGlobal("img_product_ex")||getGlobalString("img_product_ex")}function getShopTermsService(){return getLexicalGlobal("shopTermsService")||getGlobalString("shopTermsService")}function buildModalContent(){const imgProductEx=getImgProductEx(),shopTermsService2=getShopTermsService();return`
      <div class="mypage-register-modal" data-prm-root>
        <div class="mypage-register-modal-wrapper">
          <div class="body-1">
            <div class="space__between check-serial-number-title" style="align-items: center; margin-bottom: 12px;">
              <span>\uC2DC\uB9AC\uC5BC \uB118\uBC84 \uD655\uC778 \uBC29\uBC95</span>
            </div>

            <div id="check-serial-number" class="m__t_12 gap__4 body-4 text-tertiary txt__dark_gry" style="margin-bottom: 18px;">
              <img class="img-product-ex" src="${imgProductEx}" alt="img-product-ex" style="width: 100%; border-radius: 4px;">
              <div class="m__t_4 align__center">
                <div style="height: 24px;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="10" height="24" viewBox="0 0 10 24" fill="none">
                    <circle cx="5.0001" cy="12" r="1.4" fill="#7C8084"/>
                  </svg>
                </div>
                <span style="font-size: 14px; line-height: 160%; letter-spacing: -.28px;">\uC81C\uD488 \uD558\uBD80\uC5D0 \uBD80\uCC29\uB41C \uD488\uC9C8\uD45C\uC2DC \uC2A4\uD2F0\uCEE4\uC5D0\uC11C \uC2DC\uB9AC\uC5BC \uB118\uBC84\uB97C \uD655\uC778\uD558\uC138\uC694. (1,5,0\uACFC I,S,O\uC758 <span class="text-select">\uC22B\uC790</span>\uC640 <span class="text-select">\uC601\uBB38</span>\uC744 \uAD6C\uBD84\uD574 \uC8FC\uC138\uC694.)</span>
              </div>
              <div class="m__t_4 align__center">
                <div style="height: 24px;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="10" height="24" viewBox="0 0 10 24" fill="none">
                    <circle cx="5.0001" cy="12" r="1.4" fill="#7C8084"/>
                  </svg>
                </div>
                <span style="text-align:left; font-size: 14px; line-height: 160%; letter-spacing: -.28px;">\uC2DC\uB9AC\uC5BC \uB118\uBC84\uAC00 \uC190\uC0C1\uB418\uC5C8\uAC70\uB098 \uD655\uC778\uC774 \uBD88\uAC00\uB2A5\uD55C \uACBD\uC6B0, \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758 \uBC14\uB78D\uB2C8\uB2E4.</span>
              </div>
              <div class="m__t_4 align__center">
                <div style="height: 24px;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="10" height="24" viewBox="0 0 10 24" fill="none">
                    <circle cx="5.0001" cy="12" r="1.4" fill="#7C8084"/>
                  </svg>
                </div>
                <span style="text-align:left; font-size: 14px; line-height: 160%; letter-spacing: -.28px;">\uD488\uC9C8\uD45C\uC2DC\uC2A4\uD2F0\uCEE4 \uBD84\uC2E4 \uC2DC \uC7AC\uBC1C\uD589\uC740 \uC5B4\uB824\uC6B8 \uC218 \uC788\uC2B5\uB2C8\uB2E4.</span>
              </div>
              <div class="m__t_4 align__center">
                <div style="height: 24px;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="10" height="24" viewBox="0 0 10 24" fill="none">
                    <circle cx="5.0001" cy="12" r="1.4" fill="#7C8084"/>
                  </svg>
                </div>
                <span style="text-align:left; font-size: 14px; line-height: 160%; letter-spacing: -.28px; font-weight: 700;">\uC774\uC9C0\uB9AC\uD398\uC5B4, \uC561\uC138\uC11C\uB9AC \uBC0F \uC18C\uBAA8\uD488\uC740 \uC815\uD488\uB4F1\uB85D \uB300\uC0C1\uC5D0 \uD574\uB2F9\uD558\uC9C0 \uC54A\uC73C\uB098, \uAD6C\uB9E4\uC77C\uB85C\uBD80\uD130 1\uB144\uAC04 \uD488\uC9C8\uBCF4\uC99D \uC11C\uBE44\uC2A4\uAC00 \uB3D9\uC77C\uD558\uAC8C \uC81C\uACF5\uB429\uB2C8\uB2E4.</span>
              </div>
            </div>

            <div class="serial-number-box">
              <label class="label__user body-2 text-secondary" style="display: table-cell;" for="serial-number-input">\uC2DC\uB9AC\uC5BC \uB118\uBC84(S/N)</label>
              <input class="popup_input m__t_4 m__b_6 body-2" type="text" id="serial-number-input" placeholder="\uC22B\uC790+\uC601\uBB38\uC73C\uB85C \uAD6C\uC131\uB418\uC5B4 \uC788\uC2B5\uB2C8\uB2E4." data-prm-serial>
              <div class="body-4 text-error" data-prm-error></div>
            </div>

            <div class="add_product_check">
              <div class="body-4 space__between align__center">
                <div class="align__center cursor__pointer">
                  <input type="checkbox" id="checkAll" class="regi_check_all cursor__pointer" data-prm-check-all />
                  <label for="checkAll" class="cursor__pointer">\uC804\uCCB4 \uB3D9\uC758</label>
                </div>
              </div>

              <div style="width:100%; height:1px; background: #EAEDF0; margin: 4px 0px 4px 4px;"></div>

              <div class="body-4 space__between align__center txt__dark_gry hidden">
                <div class="align__center cursor__pointer">
                  <input type="checkbox" id="individual_regi_check_service" class="checkIndividual regi_check_service cursor__pointer" data-prm-check-individual />
                  <label for="individual_regi_check_service" class="cursor__pointer"><span class="terms_txt text-select">(\uD544\uC218)</span><span class="check_txt"> \uC1FC\uD551\uBAB0 \uC774\uC6A9 \uC57D\uAD00</span></label>
                </div>
                <div class="btn_show text-tertiary show_terms_service" data-prm-policy-btn="1">\uBCF4\uAE30</div>
              </div>

              <div class="body-4 space__between align__center txt__dark_gry">
                <div class="align__center cursor__pointer">
                  <input type="checkbox" id="individual_regi_check_privacy" class="checkIndividual regi_check_privacy cursor__pointer" data-prm-check-individual />
                  <label for="individual_regi_check_privacy" class="cursor__pointer"><span class="terms_txt text-select">(\uD544\uC218)</span><span class="check_txt"> \uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758</span></label>
                </div>
                <div class="btn_show text-tertiary show_privacy_policy" data-prm-policy-btn="2">\uBCF4\uAE30</div>
              </div>
            </div>
          </div>
        </div>
        <!-- \uC815\uCC45 -->
        <div class="policy-1" style="display : none" data-prm-policy="1">${shopTermsService2}</div>
        <div class="policy-2" style="display : none" data-prm-policy="2">
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
                  <td>\uC774\uB984, \uC774\uBA54\uC77C, \uD734\uB300\uD3F0 \uBC88\uD638</td>
                  <td>\uC81C\uD488 \uC815\uD488\uB4F1\uB85D, \uC81C\uD488\uBCC4 \uB9DE\uCDA4\uD615 \uCF58\uD150\uCE20 \uBC0F \uC11C\uBE44\uC2A4 \uB4F1 \uC81C\uACF5 \uB610\uB294 \uCD94\uCC9C</td>
                  <td>\uD68C\uC6D0\uD0C8\uD1F4 \uC2DC</td>
                </tr>
              </tbody>
            </table>
            <div class="terms-modal-text">
              &#8251; \uC815\uBCF4\uC8FC\uCCB4\uB294 \uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9\uC5D0 \uB3D9\uC758\uD558\uC9C0 \uC54A\uC744 \uAD8C\uB9AC\uAC00 \uC788\uC73C\uBA70, \uC120\uD0DD \uC0AC\uD56D\uC5D0 \uB300\uD55C \uB3D9\uC758\uB97C \uAC70\uBD80\uD558\uB354\uB77C\uB3C4 \uC11C\uBE44\uC2A4 \uC774\uC6A9\uC774 \uAC00\uB2A5\uD569\uB2C8\uB2E4.
            </div>
          </div>
        </div>
      </div>

      <div class="add_product_complete_wrapper">
        <div class="add_product_complete" data-prm-submit>\uC815\uD488 \uB4F1\uB85D\uD558\uAE30</div>
      </div>
    `}function getModalRoot(){return document.querySelector(".mypage-register-modal[data-prm-root]")}function normalizeSerialValue(value){return String(value||"").normalize("NFKC").replace(REGEX_SERIAL_DASHES,"-").replace(REGEX_ZERO_WIDTH,"").trim()}function updateButtonState(state){const{serialInput,checkAll,submitButton}=state;if(!serialInput||!checkAll||!submitButton)return;const serialValue=normalizeSerialValue(serialInput.value),isValid=checkAll.checked&&serialValue!==""&&REGEX_SERIAL.test(serialValue);submitButton.classList.toggle("add_activation",isValid)}function bindPolicyEvents(state){const{modalRoot,modalButton}=state,modalHeader=document.querySelector(".modal--header"),titleElement=modalHeader?modalHeader.querySelector("p"):null,policyButtons=modalRoot.querySelectorAll("[data-prm-policy-btn]"),createBackButton=()=>{const backButton=document.createElement("button");return backButton.innerHTML=`<span style="display:flex; padding: 4px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M9.1875 2.1875L4.375 7L9.1875 11.8125" stroke="white" stroke-width="1.2" stroke-linecap="square" style="mix-blend-mode:exclusion"/>
        </svg>
      </span>`,backButton.className="back-button",modalHeader&&modalHeader.prepend(backButton),backButton};policyButtons.forEach(button=>{button.addEventListener("click",()=>{const policyId=button.getAttribute("data-prm-policy-btn"),policy=modalRoot.querySelector(`[data-prm-policy="${policyId}"]`);if(!policy)return;modalRoot.querySelector(".mypage-register-modal-wrapper").style.display="none",modalButton.style.display="none",modalRoot.querySelectorAll("[data-prm-policy]").forEach(content=>{content.style.display="none"}),policy.style.display="block";const backButton=createBackButton();titleElement&&(titleElement.textContent=policyId==="1"?"\uC1FC\uD551\uBAB0 \uC774\uC6A9 \uC57D\uAD00":"\uAC1C\uC778\uC815\uBCF4 \uC218\uC9D1 \uBC0F \uC774\uC6A9 \uB3D9\uC758"),backButton.addEventListener("click",()=>{modalRoot.querySelector(".mypage-register-modal-wrapper").style.display="block",modalRoot.querySelectorAll("[data-prm-policy]").forEach(content=>{content.style.display="none"}),backButton.remove(),modalButton.style.display="block",titleElement&&(titleElement.textContent=DEFAULT_TITLE)});const closeBtn=document.querySelector(".modal--close_btn");closeBtn&&closeBtn.addEventListener("click",()=>backButton.remove(),{once:!0})})})}function bindModalEvents(state){const{modalRoot}=state,serialInput=modalRoot.querySelector("[data-prm-serial]"),submitButton=document.querySelector("[data-prm-submit]"),checkAll=modalRoot.querySelector("[data-prm-check-all]"),checkIndividuals=modalRoot.querySelectorAll("[data-prm-check-individual]"),errorText=modalRoot.querySelector("[data-prm-error]"),modalButton=document.querySelector(".add_product_complete_wrapper");state.serialInput=serialInput,state.submitButton=submitButton,state.checkAll=checkAll,state.checkIndividuals=checkIndividuals,state.errorText=errorText,state.modalButton=modalButton,serialInput&&serialInput.addEventListener("input",()=>updateButtonState(state)),checkAll&&checkAll.addEventListener("click",()=>{checkIndividuals.forEach(checkbox=>{checkbox.checked=checkAll.checked}),updateButtonState(state)}),checkIndividuals.forEach(checkbox=>{checkbox.addEventListener("change",()=>{const isAllChecked=Array.from(checkIndividuals).every(item=>item.checked);checkAll&&(checkAll.checked=isAllChecked),updateButtonState(state)})}),submitButton&&submitButton.addEventListener("click",()=>submitRegistration(state)),bindPolicyEvents(state),updateButtonState(state)}function openLoading(){typeof openLoadingModal=="function"&&openLoadingModal()}function closeLoading(){typeof closeLoadingModal=="function"&&closeLoadingModal()}function findProductBySkuInAllData(targetSku){const allProductData2=getLexicalGlobal("allProductData")||window.allProductData;if(!Array.isArray(allProductData2))return null;for(const product of allProductData2)if(product.variants&&Array.isArray(product.variants)){for(const variant of product.variants)if(variant.sku===targetSku)return variant.product_gid=product.id,variant}return null}function resolveProduct(sku,options){return options&&typeof options.findProduct=="function"?options.findProduct(sku):typeof window.findProductBySku=="function"?window.findProductBySku(sku):findProductBySkuInAllData(sku)}function getErrorMessage(code,options){const tone=options.errorTone||"normal",bundle=ERROR_MESSAGES[tone]||ERROR_MESSAGES.normal;return bundle[code]||bundle.default}function submitRegistration(state){const{serialInput,checkAll,submitButton,errorText,options}=state;if(!serialInput||!checkAll)return;const serialValue=normalizeSerialValue(serialInput.value);if(!(checkAll.checked&&serialValue!==""&&REGEX_SERIAL.test(serialValue)))return;serialInput.value=serialValue,errorText&&(errorText.innerHTML=""),openLoading(),submitButton&&(submitButton.style.pointerEvents="none");const md5Hash=getLexicalGlobal("customerMd5Hash")||window.customerMd5Hash,endpoint=options&&options.apiEndpoint?options.apiEndpoint:API_ENDPOINT;fetch(endpoint,{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({customerMd5Hash:md5Hash,serial_number:serialValue})}).then(async response=>{const resJson=await response.json();if(!response.ok)throw new Error(resJson.response_message||"\uC5D0\uB7EC \uBC1C\uC0DD");return resJson}).then(data=>{if(String(data.code)==="200")handleSuccess(data,serialValue,options);else{const code=String(data.code||"");(code==="1001"||code==="1002"||code==="1003")&&data.msg?errorText&&(errorText.innerHTML=data.msg):errorText&&(errorText.innerHTML=getErrorMessage(code,options))}}).catch(()=>{errorText&&(errorText.innerHTML=getErrorMessage("default",options))}).finally(()=>{submitButton&&(submitButton.style.pointerEvents="auto"),closeLoading()})}function handleSuccess(data,serialValue,options){const manuDt=data.data.manuDt,finishDt=data.data.finishDt,manuDate=new Date(parseInt(manuDt.substring(0,4)),parseInt(manuDt.substring(4,6))-1,parseInt(manuDt.substring(6,8))),cutoffDate=new Date(2020,5,30);let verifyDate;manuDate<cutoffDate?(verifyDate=new Date(manuDate),verifyDate.setFullYear(verifyDate.getFullYear()+1)):verifyDate=new Date(parseInt(finishDt.substring(0,4)),parseInt(finishDt.substring(4,6))-1,parseInt(finishDt.substring(6,8)));const formatted=`${verifyDate.getFullYear()}.${String(verifyDate.getMonth()+1).padStart(2,"0")}.${String(verifyDate.getDate()).padStart(2,"0")}`;typeof closeAlertModal=="function"&&closeAlertModal(),options.successMode==="simple"?showSimpleSuccess(data,options):showDetailSuccess(data,serialValue,formatted,options);const sku=`${data.data.itmCd}-${data.data.colCd}`,product=resolveProduct(sku,options),formattedManufactureDate=`${manuDate.getFullYear()}-${String(manuDate.getMonth()+1).padStart(2,"0")}-${String(manuDate.getDate()).padStart(2,"0")}`,today=new Date,formattedRegistrationDate=`${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,"0")}-${String(today.getDate()).padStart(2,"0")}`,formattedExpirationDate=`${verifyDate.getFullYear()}-${String(verifyDate.getMonth()+1).padStart(2,"0")}-${String(verifyDate.getDate()).padStart(2,"0")}`;let itemCategory="_",itemName=data.data.itmNm||"_",itemId=sku;if(product&&(itemCategory=product.category||"_",itemName=product.title||"_",itemId=product.sku||"_"),Array.isArray(window.dataLayer)){const pageTypeValue=getLexicalGlobal("pageType")||window.pageType;window.dataLayer.push({event:"register_warranty",page_type:pageTypeValue,ce_item_category:itemCategory,ce_item_name:itemName,ce_item_id:itemId,manufacture_date:formattedManufactureDate,registration_date:formattedRegistrationDate,expiration_date:formattedExpirationDate})}}function showSimpleSuccess(data,options){const referralNotice=(typeof data?.data?.referral_cd=="string"?data.data.referral_cd.trim():"")?"":`
        <div class="body-3 text-tertiary" style="margin-top: 16px;">
          \uB9AC\uD37C\uB7F4 \uCF54\uB4DC\uB294 \uBC1C\uAE09\uB418\uC9C0 \uC54A\uC740 \uC81C\uD488\uC785\uB2C8\uB2E4.
        </div>
      `,content=`
      <div class="mini-modal-center">
        <div class="mini-modal-text">
          ${options.successMessage}
        </div>
        ${referralNotice}
        <div class="mini-modal-btn complete-modal-btn">\uD655\uC778</div>
      </div>
    `;typeof openMiniModalWithContent=="function"&&openMiniModalWithContent(content,()=>{const btn=document.querySelector(".complete-modal-btn");btn&&btn.addEventListener("click",()=>{typeof closeMiniModal=="function"&&closeMiniModal(),history.go(0)})})}function showDetailSuccess(data,serialValue,formatted,options){const iconShare=getIcon("icon_share_line_bk"),iconCloseBk=getIcon("icon_close_line_bk"),iconKakao=getIcon("icon_sns_kakao"),iconLink=getIcon("icon_sns_link"),referralCode=typeof data?.data?.referral_cd=="string"?data.data.referral_cd.trim():"",shareHtml=!!(referralCode&&iconShare&&iconKakao&&iconLink&&iconCloseBk)?`
        <div class="my_product_share">
          <img class="my_product_share_img" src="${iconShare}" alt="icon-share-line-bk">
          <div class="my_product_share_menu hidden">
            <div class="my_product_share_close">
              <img src="${iconCloseBk}" alt="icon-close-line-bk">
            </div>
            <div class="my_product_share_btn" style="margin-bottom: 12px;" onclick="shareReferralCodeKakao('${referralCode}', event)">
              <div class="my_product_share_icon"><img src="${iconKakao}" alt="icon-sns-kakao"></div>
              <div>\uCE74\uCE74\uC624\uD1A1</div>
            </div>
            <div class="my_product_share_btn" onclick="copyReferralCode('${referralCode}', event, '${options.shareContainerSelector}')">
              <div class="my_product_share_icon"><img src="${iconLink}" alt="icon_sns_link"></div>
              <div>\uB9AC\uD37C\uB7F4 \uCF54\uB4DC \uBCF5\uC0AC</div>
            </div>
          </div>
        </div>
      `:"",referralHtml=referralCode?`
                  <div style="margin-top:24px;">\uB9AC\uD37C\uB7F4\uCF54\uB4DC</div>
                  <div class="space__between bg__gray" style="margin:8px 0 0 0;">
                    <div class="body-3 my-product-code" style="padding-left:4px;">${referralCode}</div>
                    ${shareHtml}
                  </div>
        `:`
                  <div class="body-3 text-tertiary" style="margin-top:24px;">\uB9AC\uD37C\uB7F4 \uCF54\uB4DC\uB294 \uBC1C\uAE09\uB418\uC9C0 \uC54A\uC740 \uC81C\uD488\uC785\uB2C8\uB2E4.</div>
        `,content=`
      <div class="mini-modal-center">
        <div class="mini-modal-text">
          ${options.detailSuccessText}
        </div>
        <div style="width: 290px; text-align: left; margin-top: 32px;">
          <div class="header__product">
            <div class="wrap_product_card">
              <div class="gap__61 my_product_text" style="display: flex; flex-direction: column; justify-content: space-between;">
                <div class="body-3">
                  <div>\uC81C\uD488\uCF54\uB4DC<span class="text-tertiary" style="margin-left:4px;">${data.data.itmCd}</span></div>
                  <div>\uC0C9\uC0C1\uCF54\uB4DC<span class="text-tertiary" style="margin-left:4px;">${data.data.colCd}</span></div>
                  <div>
                    \uD488\uC9C8\uBCF4\uC99D\uAE30\uAC04
                    <span class="text-tertiary" style="margin-left:4px;"><span class="text-select">${formatted}</span>\uAE4C\uC9C0</span>
                  </div>
                  <div>
                    \uC2DC\uB9AC\uC5BC\uB118\uBC84<span class="text-tertiary" style="margin-left:4px;">${serialValue}</span>
                  </div>
                  ${referralHtml}
                </div>
              </div>
            </div>
          </div>
        </div>
        <div style="display:flex; gap:8px;">
          <div class="mini-modal-btn" onclick="location.href='${options.detailPrimaryCtaUrl}'">${options.detailPrimaryCtaText}</div>
          <div class="mini-modal-btn complete-modal-btn">${options.detailSecondaryCtaText}</div>
        </div>
      </div>
    `;typeof openMiniModalWithContent=="function"&&openMiniModalWithContent(content,()=>{miniModalOpenShare(),miniModalCloseShare();const btn=document.querySelector(".complete-modal-btn");btn&&btn.addEventListener("click",()=>{typeof closeMiniModal=="function"&&closeMiniModal(),history.go(0)})})}function openModal(options){const resolved=resolveOptions(options);if(typeof openModalWithContent!="function")return;const modalContent=buildModalContent();openModalWithContent(resolved.title,modalContent,()=>{const modalContents=document.querySelector(".modal--contents");modalContents&&(modalContents.style.height="auto",modalContents.style.marginBottom="100px");const modalRoot=getModalRoot();modalRoot&&(activeState={modalRoot,options:resolved},bindModalEvents(activeState))})}function miniModalOpenShare(){document.querySelectorAll(".mini-modal-center .my_product_share_img").forEach(btn=>{btn.addEventListener("click",e=>{const menu=e.currentTarget.parentNode.querySelector(".my_product_share_menu");menu&&menu.classList.remove("hidden")})})}function miniModalCloseShare(){document.querySelectorAll(".mini-modal-center .my_product_share_close img").forEach(btn=>{btn.addEventListener("click",e=>{const menu=e.currentTarget.closest(".my_product_share_menu");menu&&menu.classList.add("hidden")})})}function shareReferralCodeKakao(code){window.Kakao&&typeof window.Kakao.isInitialized=="function"&&window.Kakao.isInitialized()&&window.Kakao.Share.sendCustom({templateId:117244,templateArgs:{code}})}function copyReferralCode(code,event,where){const targetSelector=where||DEFAULT_OPTIONS.shareContainerSelector;document.querySelectorAll(".share-popup-container").forEach(el=>el.remove());const parentTemp=event?.currentTarget?.parentNode,iconCloseWh=getIcon("icon_close_line_wh"),popupContent=`
      <div class="share-popup-container">
        <div class="share-popup-text">\uCF54\uB4DC\uAC00 \uBCF5\uC0AC\uB418\uC5C8\uC2B5\uB2C8\uB2E4</div>
        <div class="share-popup-close">
          ${iconCloseWh?`<img src="${iconCloseWh}" alt="icon_close_line_wh" />`:""}
        </div>
      </div>`;navigator?.clipboard?.writeText&&navigator.clipboard.writeText(code).then(()=>{parentTemp&&parentTemp.classList.add("hidden");const container=document.querySelector(targetSelector);if(container){container.insertAdjacentHTML("beforeend",popupContent);const closeBtn=container.querySelector(".share-popup-close img");closeBtn&&closeBtn.addEventListener("click",()=>{const popup=container.querySelector(".share-popup-container");popup&&popup.remove()})}})}window.ProductRegisterModalLegacy={open:openModal,submit:()=>{activeState&&submitRegistration(activeState)}},typeof window.openProductRegisterModal!="function"&&(window.openProductRegisterModal=openModal),window.findProductBySkuInAllData=findProductBySkuInAllData,window.miniModalOpenShare=miniModalOpenShare,window.miniModalCloseShare=miniModalCloseShare,window.shareReferralCodeKakao=shareReferralCodeKakao,window.copyReferralCode=copyReferralCode,window.addProductProceed=()=>{activeState&&submitRegistration(activeState)}})();
//# sourceMappingURL=/cdn/shop/t/152/assets/product-register-modal-legacy.js.map
