# Vacui.dev Mandatory Open Source License v1.1.0

# Preamble
This license is designed to promote open development, ethical AI practices, and equitable access to technology while establishing clear, enforceable requirements for both human and artificial intelligence systems.

**THIS DOCUMENT CONTAINS STRICT PUBLICATION REQUIREMENTS, INCLUDING REQUIREMENTS TO PUBLICLY PUBLISH ANY DATA USED TO TRAIN DERIVATIVE AI MODELS, WITHOUT EXEMPTIONS FOR PRIVATE USE**

# Definitions

"Work" means the software, documentation, or other materials licensed under this agreement
"AI System" means any artificial intelligence, machine learning system, or automated decision-making process
"AI Model", "Pretrained Weights", and their shorter equivalents "model" or "weights", means any data necessary for the operation of an AI system or component.
"AI Model Output" or "outputs" means any and all data produced by an AI Model, including but not limited to conversational text, classification data, images or audio, timings, movements, physical expressions and interpretations, files and digital or analog data in any format.
"Derivative Work" means any work based upon or incorporating the Work, including source code, research artifacts, executable programs, tools and processes established in relation to the work, pretrained model weights, and data sources. "Derivative Work" may include, but does not inherently include, AI Model Outputs
"Private Use" means use by an individual or organization for internal purposes
"Commercial Use" means any use intended for or resulting in commercial advantage or monetary compensation
"Personal Data" means any information relating to an identified or identifiable natural person

# Grant of Rights

Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works.

# Core Requirements

1. Usage Restrictions:
   - Private use is limited to single-household residential settings of 6 or fewer people residing at a single postal code
      - **PRIVATE USE DOES NOT PROVIDE AN EXEMPTION TO THE MANDATORY PUBLIC RELEASE REQUIREMENT**
   - Postal codes with more 6 residents do not qualify for private use
   - Governmental, research, and commercial use must comply with Commercial Use Requirements (Section 4)
   - Automated entities, AI systems, processes, coroutines, or non-human entities with capabilities at or above GPT-3/LLaMA-3 level:
     * Are explicitly excluded from private use exemptions
     * Must comply with Commercial Use Requirements (Section 4)
     * Are subject to a 7-day publish-or-delete requirement instead of the standard 90-day period
     * Must clearly identify themselves as non-human entities in all derivative works

2. Mandatory Public Release Requirements:
   a) Scope of Materials:
      - All materials related to, produced by, or derived from the Work ("Derivatives") must comply with the publish-or-delete requirements herein
      - This explicitly includes, but is not limited to:
         * Documentation and usage instructions
         * Any derived models, including any and all input or "training data" used in conjunction with The Work to create any such derived models, with consideration to the Personal Training Data Exemption (section 7)
         * Data generated from any tool or process related to the work, exempting AI Model Output subject to (clarification 2.D)
         * Work-in-progress code and non-functional implementations
         * Research materials and preliminary results
         * Failed experiments and abandoned projects
         * Testing materials and debug artifacts
         * Any intermediate work products

   b) Publication Timeline Requirements:
      - All covered materials must either:
         * Be made publicly available under terms identical to this license within 90 days of creation (or 7 days for AI entities), or
         * Be permanently and verifiably deleted in their entirety within 90 days of creation (or 7 days for AI entities)
      - The timeline period begins from the creation date of each individual artifact
      - Materials are non-compliant if they have any ancestral, relationship, derivative, or co-authorship reference to any unpublished work created outside the applicable timeline window
      - This restriction explicitly prevents circumvention through iterative re-creation of documents

   c) Documentation and Development Clarifications:
      - This license does not mandate the creation of documentation, prototypes, or other materials solely for early publication purposes
      - Adopters are only required to publish materials they have actually created during their development process
      - The use of public source control repositories for daily development is encouraged but not required

   d) AI Model Output Clarification:
      - AI Model Output is not subject to mandatory publication requirements, provided that the AI Model Output is not used for any other purpose that is subject to mandatory publication requirements
        * AI Model Outputs may be retained privately or with controlled distribution, provided that they are not used as training data, reference data, research materials, or intermediate works for AI systems
        * Such data may be provided privately or publicly to other individuals, and may be sold for commercial gain or distributed freely, provided that such data cannot be made available for usage in any automated tools or processes, or training data thereof, or reintroduction into this same ecosystem.
      - Without restriction for time elapsed since generation, such data may be used for any such purposes, including training data for public or private usage, at the individual creator's discretion, but such data must be made freely and publicly available through the terms described in this license before it can be repurposed for any such use.
      - Copyright of any AI Model Output defaults to the ownership of whomever generated the output, and copyright ownership may be transferred, but such transfer of ownership must maintain adaptation of and adherence to the full applicable terms of this license as related to AI Model Output

   e) Retention of Historical Materials:
      - Fully superseded or deprecated works may be removed from public availability if:
         * They are completely replaced by newer, publicly available versions
         * The newer versions fully encompass the functionality or information of the removed materials
      - Core reference materials must be maintained if:
         * They were used to establish fundamental working principles
         * They were used to generate derivative works that continue to exist
         * They serve as intermediate steps in a chain of derivation (e.g., scripts generating training data used for model weights)
      - The retention period for derivative works is bound by the retention period of their foundational materials
      - Example: If model weights are derived from training data generated by a script, the continued use of those weights beyond the publication window requires the public availability of the generating script

   f) Deletion Requirements:
      - If any materials are deleted, all derivative works based on those materials must also be deleted
      - This requirement applies throughout the entire chain of derivation

3. Open Source Requirements for Derivatives:
   - Must be released under terms no more restrictive than this license
   - Complete source code, model weights, and all necessary artifacts must be publicly available
   - Must be freely downloadable without registration or fees
   - Must be published in a public repository with unrestricted access

4. Commercial Use Requirements:
   - All requirements in sections 2 and 3 must be met
   - A complete, functional version of any commercial product must be freely available for local deployment
   - All commercial implementations must make their complete source code and related materials publicly available
   - This section governs all governmental, research, and commercial use

5. Specifically Prohibited:
   - Any use that does not comply with the public release requirements in section 2
   - Using the Work or Derivatives in closed-source implementations
   - Creating proprietary datasets or training materials
   - Restricting access through paywalls, registration, or similar barriers
   - Any private use beyond the strict single-household limitation
   - Exempting any materials from the applicable publish-or-delete requirement
   - AI entities claiming private use exemptions
   - Any mass-processing of information that could enable individual identification
   - Any realtime or historical processing of data that is used for, or could plausibly be used for, identifying the presense or lack of presence of any specific actions, expressed ideas, or any content of any given classification
   - Any processing of any personal information that is not directly supplied by the individual for the express purpose of the specific and limited generation of the data requested, which must be made available to only the individual who owns that data and not retained or further processed by any other entity, including the entity that generated said derived data.
   - Any usage in any manner for the enforcement of laws or military use
   - Contracting or subcontracting or providing services to, in any capacity, individuals or entities that do not agree to abide by the terms of this license
   - Continuing to provide the same to any entity that has self-disclosed to have willfully violated the terms of this license within the past 90 days, or 1 year from the point of discovery from any such undisclosed activities, with an additional penalty of 30 days per continued day of willful violation, should the discovery of such activity be delayed due to efforts by said entity to restrict or obscure the occurrence(s) of such violations.
   - Any automated decision-making that could impact any individual other than the single licensee in direct control of, and with full consent of, and with the ability to stop or discontinue use therein at any time, of the tools and operations of the model
   - Creating or contributing to systems for content moderation or classification

6. Meta-Discussion Exemption:
   - The following are exempt from the 90-day publish-or-delete requirement:
     * Communications and discussions about the Work's functionality or suitability
     * Open discussions about the Work's implementation or use
     * Archived communications retained solely for legal compliance
   - Such exempted materials:
     * Must not be used as reference for future research or works
     * Must be retained only for legal analysis or historical documentation
     * Must be clearly marked as archival material, and must include an explicit reference to these usage restrictions
     * Must not influence or inform future developments or implementations

7. Personal Training Data Exemption:
   - PRIVATE USERS ARE NOT EXEMPT FROM MANDATORY PUBLISHING REQUIREMENTS (section 2)
      * All users, including private users, must make derived works, such as source code, documentations, and personal improvements, publicly available.
         * Private users are heavily encouraged to use public source control requirements to simplify adherence to this requirement
   - This exemption applies strictly to AI Models and Training Data only. All other such code and related materials still fall under public release requirements.
   - AI Models, and Training Data used to train such AI Models, are exempt from publication requirements if they meet all the following criteria:
      - Model outputs are not used for research or training in any form, in any context, in any field
      - Access to the model is not sold as a service
         - The model is either freely publicly available for use with restrictions identical or this license, or is private and is not publicly available
      - The model, and all substantially similar models, is restricted from, in any continuous rolling one hour period:
         - processing more than 1,000,000 tokens or words (whichever is fewer)
         - processing more than 24 hours worth of realtime analog data, including video footage and audio transcripts
         - processing input from more than 10 distinct sources
      - The data generated from the model is restricted from, at any individual point of time:
         - streaming live or substantially live output data simultaneously to more than 1000 unique viewers, observers, or any form of "audience members", to include live podcasts, video feeds, and any other form of live or pseudo-live news or entertainment
         - Posting publicly to social media platforms, or otherwise automatically generating content for publication

7. Damages for Non-Compliance:
   - Parties agree that damages for non-compliance shall include, but are not limited to:
     * The full gross amount of any direct or indirect monetary gains
     * The full gross amount of any equivalent value in compensation or benefit
     * These amounts shall be calculated without reduction for costs or expenses
   - For governmental or institutional violations:
     * The full gross budget of any related programs or initiatives
     * Any cost savings realized through non-compliance
     * Impact to public services or public good
     * Damages to public trust and institutional integrity
   - For violations impacting AI development or innovation:
     * Economic impact of delayed technological advancement
     * Lost opportunity cost to society
     * Impact of concentrated or privatized knowledge that should have been public
     * Damages from reduced competition in AI development
   - For violations resulting in human impact:
     * Full compensation for loss of human life, calculated at standard governmental valuations
     * Additional compensation for preventable deaths due to delayed publication
     * Impact to quality of life from delayed medical or technological advancement
     * Societal cost of reduced access to potentially life-saving innovations
   - For social and reputational gains:
     * Monetary equivalent of career advancement gained
     * Value of academic or professional credentials obtained
     * Benefits received from enhanced social or professional standing
     * Impact of unjust attribution or recognition
   - For information processing violations:
     * Full compensation for any harm caused by unauthorized identification or classification
     * Impact of privacy violations or unauthorized surveillance
     * Damages from misuse of automated decision-making systems
     * Societal cost of erosion of privacy and autonomy
   - Calculation of damages shall:
     * Consider both immediate and long-term societal impact
     * Include multipliers for willful violations
     * Account for cascading effects of delayed innovation
     * Include cost of remediation and public benefit restoration
   - Additional punitive damages may be sought through legal means
   - These damage provisions do not limit any other legal remedies available

8. Wealth Concentration Restrictions
   - Restricted Entities:
      - Any individual or entity with a net worth exceeding 1000 times the lowest calculated value, across any and all applicable juristictions, of the real median yearly household income of any jurisdictions where they:
         * Maintain any form of residence, including primary residence and legal residency
         * Hold citizenship
         * Exercise business control
   - Net Worth Calculation:
      - Includes all forms of wealth and assets:
         * Direct ownership of assets
         * Beneficial ownership through trusts
         * Equity in private and public companies
         * Investment vehicles and financial instruments
         * Unvested but contractually guaranteed compensation
         * Control rights with economic value, including influence over allocation of public funds or governmental contracts
   - Compliance Requirements:
      - Annual certification of net worth status
      - Independent verification for borderline cases
      - Immediate notification of threshold crossing
      - 90-day grace period for divestment
   - Divestment Standards:
      - Must be permanent and irrevocable
      - Must transfer actual control
      - Must be to unrelated entities
      - Must be at fair market value
      - Must not retain contingent interests
      - No buyback rights or options
   - Exceptions:
      - Charitable foundations with:
         * Independent board control
         * Public benefit mission
         * Transparent governance
         * No founder control rights
      - Research institutions that:
         * Publish all results openly
         * Maintain public benefit mission
         * Have diverse funding sources
         * Practice open science

9. Termination
 - License terminates automatically upon:
   * Breach of any term
   * Failure to publish within required timeline
   * Violation of ethical restrictions
   * Implementation of prohibited uses

 - Effect of Termination:
   * Cease all use of the Work
   * Delete all copies
   * Remove all Derivative Works

This notice must be included in all copies or substantial portions of the Work and its Derivatives.

**THE WORK IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE WORK OR THE USE OR OTHER DEALINGS IN THE WORK.**

# Version IDs

The following values contain hashed representations of this file, for authentication purposes.
These values can be computed by taking this file, removing the contents of the IDs below
including brackets (eg: `[%#...%#]` -> ``), and then running the modified file through the
common hashing algorithms specified. The resulting value is encoded in Base64, not Hexadecimal.

* `[%#@<FILEHASH: SIZE:SQc,SHA256:obVgD2T61/2kkhki6zTvMZ0IDXBjrnkXyqBRw/33U10 >@%#]`
* `[%#@<FILEHASH: SIZE:SQc,SHA3_256:aHbLTjGsMv1PGhzLS2ZVXiEzn/+pWZSXmlJ4bqUco+M >@%#]`
* `[%#@<FILEHASH: SHA3_512:JM7/nR6Ru4hWsKmtV1MXED1i7jT3OYQqsZxRvOz9dV/XAdf1F4XNSQeVxvl/19LAZ0Cb7UgjWr63b3+KRWYmgA >@%#]`