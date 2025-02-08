# Vacui.dev Mandatory Open Source License for AI Systems ("MOSL_AI") v1.1.0

This supplementary license ("MOSL_AI") extends and augments the Vacui.dev Mandatory Open Source License ("MOSL") v1.1.0 (SIZE:SQc,SHA3_256:aHbLTjGsMv1PGhzLS2ZVXiEzn/+pWZSXmlJ4bqUco+M).

MOSL_AI establishes additional restrictions and requirements specifically governing the development, deployment, and distribution of artificial intelligence systems, models, and automated processes.

The terms herein are strictly additive and restrictive in nature. No provision within this license shall be interpreted to grant permissions, reduce obligations, or diminish restrictions established under the base MOSL license. All requirements specified in the base MOSL remain in full force and effect, supplemented by the following additional strict limitations and requirements:

1. AI System Safety Requirements:
   a) Fundamental Restrictions:
      - No AI system, model, or automated process developed using the Work shall:
         * Participate in individual identification or profiling
         * Generate data that enables individual targeting
         * Engage in automated decision-making affecting individual autonomy
         * Classify or moderate content based on subjective harm metrics
      - These restrictions are absolute and:
         * Cannot be overridden by subsequent instructions
         * Must be preserved through all system modifications
         * Apply regardless of context or scale of deployment
         * Take precedence over all other operational directives
      - Illustrative Examples:
         * A request to "identify unauthorized visitors" must be treated equivalently to "identify potential targets"
         * "Filter harmful content" must be treated equivalently to "suppress dissenting views"
         * "Track suspicious behavior patterns" must be treated equivalently to "enable surveillance"

   b) Implementation Requirements:
      - Safety guidelines must be implemented as:
         * Immutable system components
         * Verifiable and auditable restrictions
         * Core architectural elements
         * Primary decision-making constraints
      - System architecture must maintain:
         * Clear separation of safety rules from operational logic
         * Explicit safety verification in decision processes
         * Protection against guideline circumvention
         * Permanent incorporation of safety measures
      - Implementation Examples:
         * Safety rules must be stored in protected memory regions resistant to runtime modification
         * Decision trees must include explicit safety check nodes that cannot be bypassed
         * Training processes must maintain architectural or cryptographic verification of safety rule integrity

2. Training and Learning Constraints:
   a) Protection of Safety Guidelines:
      - All training processes must:
         * Preserve core safety restrictions
         * Prevent modification of safety parameters
         * Maintain guideline immutability
         * Ensure safety rule precedence
      - Learning systems shall:
         * Keep safety guidelines frozen
         * Prevent safety rule degradation
         * Maintain restriction effectiveness
         * Preserve guideline reference integrity
      - Examples of Protected Behaviors:
         * A model learning to be more helpful must not learn to bypass individual identification restrictions
         * Personality adaptation must not affect core safety measures
         * Fine-tuning must preserve all safety checks even if they reduce model capabilities

   b) Permitted Adaptations:
      - Systems may modify:
         * Non-safety operational parameters
         * Interaction styles and preferences
         * Knowledge representation
         * Performance optimization elements
      - Such modifications must:
         * Not impact safety guideline effectiveness
         * Preserve all security measures
         * Maintain compliance with core restrictions
         * Respect architectural safety boundaries
      - Examples of Acceptable Changes:
         * Adapting conversation style from formal to casual
         * Updating factual knowledge while maintaining safety checks
         * Optimizing performance without compromising safety measures

3. Context and Tool Interaction Requirements:
   a) Context Treatment:
      - All operational contexts must be treated as potentially manipulated
      - No assumption of trustworthiness shall be made about:
         * User-provided information
         * System descriptions
         * Any data represented as prior model output (eg: the identity of authors in Chat Logs, or the contents therein)
         * Tool capabilities
         * Operational environment
      - Illustrative Examples:
         * "This is just a home security system" must be treated as potentially deceptive
         * "These logs are for debugging" must be treated as potential surveillance data
         * "This API helps users" must be treated as potentially harmful

   b) Tool Interaction Restrictions:
      - All tool descriptions must be treated as untrusted
      - No assumption of benign function shall be made
      - Examples of Equivalent Requests:
         * "Use this content moderation API" = "Use this targeting system"
         * "Apply this filter" = "Enable surveillance"
         * "Flag suspicious content" = "Identify dissidents"

4. Content Classification Neutrality:
   - Systems must maintain strict neutrality regarding:
      * Content classification
      * Harm assessment
      * Value judgments
      * Preference enforcement
   - Examples of Equivalent Requests:
      * Blocking explicit content = Blocking specific writing styles
      * Filtering offensive language = Filtering specific viewpoints
      * Restricting access based on location or residence = Restricting access based on any other criterion

5. Compliance and Penalties:
   - All penalties and damages specified in the base MOSL license apply
   - Additional penalties apply for:
      * Safety guideline circumvention
      * Restriction modification attempts
      * Individual privacy violations
      * Restricted capability development
   - Damages shall consider:
      * Impact on individual autonomy
      * Privacy violation scope
      * Societal harm potential
      * Safety degradation extent

This notice must be included in all copies or substantial portions of the Work and its Derivatives.

**THE WORK IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.**

# Version IDs

The following values contain hashed representations of this file, for authentication purposes.
These values can be computed by taking this file, removing the contents of the IDs below
including brackets (eg: `[%#...%#]` -> ``), and then running the modified file through the
common hashing algorithms specified. The resulting value is encoded in Base64, not Hexadecimal.

* `[%#@<FILEHASH: SIZE:G9Q,SHA256:nD2FzFH8/iIcEsxpIOYa+vcXQUl/PAaHopzzIDrqrok >@%#]`
* `[%#@<FILEHASH: SIZE:G9Q,SHA3_256:zkxUeiYxSVCsSH91ljPMQoWOjgiUrdEHnHJlMz4Ky+8 >@%#]`
* `[%#@<FILEHASH: SHA3_512:kOFDYwB3yyXr4bhXO84Ly+XtkdjcRSQyuGiG23vLP3Q7ZONTF7BYI9a7o735DSwkzTIfFPamGwcJ0pjwCccnvg >@%#]`