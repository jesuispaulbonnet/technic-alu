// Include gulp
var gulp = require('gulp');
var sass = require('gulp-sass');
var rename = require('gulp-rename');
var minify = require('gulp-minify');


// Compile Sass
gulp.task('sass', function() {
    return gulp.src('technic_alu/static/sass/technic_alu.scss')
        .pipe(sass({outputStyle: 'compressed'}))
        .pipe(rename('technic_alu.min.css'))
        .pipe(gulp.dest('technic_alu/static/css'));
});
// Minify javascript
gulp.task('scripts', function() {
  gulp.src('technic_alu/static/js/*')
    .pipe(minify({
      ext: {
          min:'.min.js'
      },
    }))
    .pipe(gulp.dest('technic_alu/static/dist/'));
});

//Watch task
gulp.task('watch', function() {
    gulp.watch('technic_alu/static/sass/**/*.scss', ['sass']);
    gulp.watch('technic_alu/static/js/**/*.js', ['scripts']);
});
