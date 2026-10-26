# Roof and Chimney Doctor website

Static multi-page site for roofandchimneydoctor.ie. No build step needed to host it: upload the folder as-is (Vercel, Netlify, any web host).

- Pages: Home, Services, the 6 service pages (same addresses as the old site, e.g. `/service/roof-repairs/`), Projects, Contact, Privacy Policy.
- Phone, email and the form settings are at the top of `assets/site.js`.
- Forms: paste a free Web3Forms access key into `formKey` in `assets/site.js` to receive enquiries by email. Until then, forms open the visitor's email app pre-filled.
- To change page text, edit `build.py` and run `python3 build.py` to regenerate the HTML.
- The lightning intro plays once per visit on the home page (add `?intro` to the URL to replay it).
