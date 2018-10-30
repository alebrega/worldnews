<?php

// Exit if accessed directly
if ( !defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Single Posts Template
 *
 *
 * @file           single.php
 * @package        Responsive
 * @author         Emil Uzelac
 * @copyright      2003 - 2014 CyberChimps
 * @license        license.txt
 * @version        Release: 1.0
 * @filesource     wp-content/themes/responsive/single.php
 * @link           http://codex.wordpress.org/Theme_Development#Single_Post_.28single.php.29
 * @since          available since Release 1.0
 */

get_header(); ?>

<div id="content" class="<?php echo esc_attr( implode( ' ', responsive_get_content_classes() ) ); ?>">

	<?php //get_template_part( 'loop-header', get_post_type() ); ?>

	<?php if ( have_posts() ) : ?>

		<?php while( have_posts() ) : the_post(); ?>

			<?php responsive_entry_before(); ?>
			<div id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
				<?php responsive_entry_top(); ?>
                             <?php the_title( '<h1>', '</h1>' );  ?>
<!-- Go to www.addthis.com/dashboard to customize your tools -->
<div class="addthis_native_toolbox"></div>
				<?php //get_template_part( 'post-meta', get_post_type() ); ?>

				<div class="post-entry">
                                   
                                    <div style="width:320px;float:right;margin-bottom:15px;margin-top:-10px;margin-left:20px;margin-right:-20px;">
                                  <script src="http://www.googletagservices.com/tag/js/gpt.js"> googletag.pubads().enableSyncRendering(); googletag.enableServices(); googletag.pubads().display("/25379366/ADT_Placement_guia9.com-300x250_2156--28355686", [300, 250], "div-gpt-ad-%%CACHEBUSTER%%-0","%%CLICK_URL_UNESC%%"); </script>

</div>
                                    
					<?php the_content( __( 'Read more &#8250;', 'responsive' ) ); ?>
                                        <div style="text-align:center;padding-top:10px;padding-bottom: 20px;">
<a href="#" onclick="ga('send', 'event', 'facebook', 'Share bottom-post BIG BUTTON', href);
        ga('send', 'event', 'exp-bottom', 'Share bottom-post BIG BUTTON', href);
        ga('global.send', 'event', 'facebook', 'Share bottom-post BIG BUTTON', href);
        ga('global.send', 'event', 'exp-bottom', 'Share bottom-post BIG BUTTON', href);
        window.open(
        'https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent('<?php echo 'http://'.$_SERVER[HTTP_HOST].$_SERVER[REQUEST_URI]; ?>'), 
        'facebook-share-dialog', 
        'width=626,height=436'); 
        return false;"><img src="<?php echo get_template_directory_uri(); ?>/images/botongrandeface.png" style="border:0px;"></a>
</div>
                                    
                                    <div style="width:100%;text-align:center;">
                                    
                                 <!-- BEGIN JS TAG - guia9.com - 300x250bis - 300x250 < - DO NOT MODIFY -->
<SCRIPT SRC="http://ads.mediafem.com/ttj?id=4056344&gender=f&cb=[CACHEBUSTER]&pubclick=[INSERT_CLICK_TAG]&referrer=[REFERRER_URL]" TYPE="text/javascript"></SCRIPT>
<!-- Begin comScore Tag -->
<script>
    var _comscore = _comscore || [];
    _comscore.push({ c1: "8", c2: "16057095" ,c3: "1015" });
    (function() {
        var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
        s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
        el.parentNode.insertBefore(s, el);
    })();
</script>
<noscript>
    <img src="http://b.scorecardresearch.com/p?c1=8&c2=16057095&c3=1015&c15=&cv=2.0&cj=1" />
</noscript>
<!-- End comScore Tag -->
<img src="http://bcp.crwdcntrl.net/5/c=3455/genp={insert channel name}" width="1" height="1"/>
<!-- END TAG -->



                                    </div>
            <?php related_posts(); ?>

					<?php if ( get_the_author_meta( 'description' ) != '' ) : ?>

						<div id="author-meta">
							<?php if ( function_exists( 'get_avatar' ) ) {
								echo get_avatar( get_the_author_meta( 'email' ), '80' );
							} ?>
							<div class="about-author"><?php _e( 'About', 'responsive' ); ?> <?php the_author_posts_link(); ?></div>
							<p><?php the_author_meta( 'description' ) ?></p>
						</div><!-- end of #author-meta -->

					<?php endif; // no description, no author's meta ?>

					<?php wp_link_pages( array( 'before' => '<div class="pagination">' . __( 'Pages:', 'responsive' ), 'after' => '</div>' ) ); ?>
				</div><!-- end of .post-entry -->
                                
                                  

				<?php //get_template_part( 'post-data', get_post_type() ); ?>

				<?php responsive_entry_bottom(); ?>
			</div><!-- end of #post-<?php the_ID(); ?> -->
                        <h3 class="titularh3">¿Que Piensas?</h3>
                        <div class="fb-comments" data-href="<?php echo 'http://'.$_SERVER[HTTP_HOST].$_SERVER[REQUEST_URI]; ?>" data-width="600" data-numposts="10" data-colorscheme="light"></div>
			<?php responsive_entry_after(); ?>

			<?php //responsive_comments_before(); ?>
			<?php //comments_template( '', true ); ?>
			<?php //responsive_comments_after(); ?>

		<?php
		endwhile;

		get_template_part( 'loop-nav', get_post_type() );

	else :

		get_template_part( 'loop-no-posts', get_post_type() );

	endif;
	?>

</div><!-- end of #content -->

<?php get_sidebar(); ?>
<?php get_footer(); ?>
